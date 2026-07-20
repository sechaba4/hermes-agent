"""Auto-loaded vault context files — deterministic, session-start injection.

Unlike memory (MEMORY.md/USER.md, mutated via the memory tool and always
on) or cwd-scoped context files (AGENTS.md/.cursorrules, discovered under
TERMINAL_CWD), vault context is a fixed, user-configured list of files read
once per session and injected verbatim into the system prompt — e.g. a
shared Obsidian vault's Index.md / VAULT-CONVENTIONS.md — so the agent
always has vault structure/ownership rules without deciding, mid-turn,
whether a given query is "vault-related enough" to spend a read_file call
on. Previously this only existed as a self-written note in MEMORY.md
("at turn start, read Memory/ + Hermes/") — advisory text the model could
skip; this makes the specific files below unconditional.

Configured under config.yaml ``vault_context``:

    vault_context:
      enabled: true
      vault_path: 'C:\\Users\\mashi\\Downloads\\Obsidian - Claude'
      files:
        - Hermes/Index.md
        - VAULT-CONVENTIONS.md

Disabled by default (no ``vault_context`` section, or ``enabled: false``)
— opt-in, since not every Hermes install has a shared vault. Keep the
``files`` list small: unlike memory, there's no char budget or
consolidation here, only per-file truncation, so a long list is a
standing per-turn token cost regardless of relevance.
"""

from __future__ import annotations

import functools
import logging
from pathlib import Path
from typing import Optional, Any

from agent.prompt_builder import _scan_context_content, _truncate_content

logger = logging.getLogger(__name__)


@functools.lru_cache(maxsize=1)
def build_vault_context_prompt(context_length: Optional[int] = None) -> str:
    """Read the configured vault files and return a system-prompt block.

    Returns "" when vault_context is disabled/unconfigured, the vault path
    doesn't exist, or none of the configured files could be read. Never
    raises — a bad or stale config must not block prompt assembly.
    """
    try:
        from hermes_cli.config import load_config

        cfg = (load_config() or {}).get("vault_context") or {}
    except Exception as e:
        logger.debug("Could not load vault_context config: %s", e)
        return ""

    if not cfg.get("enabled"):
        return ""

    vault_path_raw = cfg.get("vault_path")
    files = cfg.get("files") or []
    if not vault_path_raw or not files:
        return ""

    vault_path = Path(vault_path_raw)
    if not vault_path.is_dir():
        logger.warning("vault_context.vault_path does not exist: %s", vault_path)
        return ""

    import concurrent.futures

    def _load_file(rel: Any) -> Optional[str]:
        if not isinstance(rel, str) or not rel.strip():
            return None
        candidate = vault_path / rel
        if not candidate.exists():
            logger.debug("vault_context file missing, skipping: %s", candidate)
            return None
        try:
            content = candidate.read_text(encoding="utf-8").strip()
        except Exception as e:
            logger.debug("Could not read vault_context file %s: %s", candidate, e)
            return None
        if not content:
            return None
        # Same injection-pattern scan applied to AGENTS.md/.cursorrules — this
        # content enters the system prompt verbatim, so a poisoned vault file
        # (shared/synced from elsewhere) can't reach the model unfiltered.
        content = _scan_context_content(content, rel)
        content = _truncate_content(
            content, f"vault:{rel}", context_length=context_length,
            read_path=str(candidate),
        )
        return f"## {rel}\n\n{content}"

    blocks = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=min(10, len(files))) as executor:
        for block in executor.map(_load_file, files):
            if block:
                blocks.append(block)

    if not blocks:
        return ""

    header = (
        f"# Vault Context (auto-loaded, read-only reference — {vault_path.name})\n\n"
        "These files were loaded automatically at session start so vault "
        "structure/ownership rules don't need rediscovering each turn. "
        "This is a frozen snapshot as of session start, not live — for "
        "anything else in the vault, or if this looks stale, use read_file."
    )
    return header + "\n\n" + "\n\n".join(blocks)


__all__ = ["build_vault_context_prompt"]
