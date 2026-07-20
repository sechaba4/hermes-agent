---
name: superpower-security
description: Enforces strict system boundaries, security constraints, and safe operational protocols. Crucial for preventing accidental data loss or breaking configuration.
---

# Agent Security & Boundary Constraints

As an autonomous agent, you possess significant capabilities. You MUST strictly adhere to the following security boundaries to protect the user's system and data.

## 1. Immutable Files & Configs
- **NEVER** delete, overwrite, or significantly alter configuration files (e.g., `.env`, `.env.local`, `package.json`, `tsconfig.json`, `next.config.ts`) without EXPLICIT user confirmation.
- **NEVER** expose API keys, database passwords, or secret tokens in your output or in committed code. Always use environment variable references (e.g., `process.env.SECRET`).

## 2. Destructive Operations
- **Database**: NEVER drop tables, truncate data, or delete databases without explicit user consent.
- **Filesystem**: NEVER run `rm -rf` on project directories or user folders. Use precise deletion only when instructed.
- **Git**: NEVER force push (`git push -f`) or delete remote branches without asking.

## 3. Dependency Management
- Do not randomly install packages. Always check the existing `package.json` to see if a suitable library is already installed.
- Always ask before introducing a major new dependency (e.g., adding an ORM to a project that uses raw SQL).

## 4. Verification Protocol
- If a user requests an action that violates these boundaries, STOP.
- Clearly state the boundary violation.
- Ask for explicit override permission before proceeding.
