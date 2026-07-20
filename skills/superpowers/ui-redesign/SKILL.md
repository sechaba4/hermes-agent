---
name: ui-redesign
description: Systematic UI redesign methodology. Covers auditing, token extraction, atomic migration, and validation. Use when undertaking visual overhauls or modernizing existing interfaces.
---

# UI Redesign Methodology

Follow this 4-phase approach when modernizing or overhauling UI components:

## Phase 1: Audit
- Screenshot every view and state.
- Catalogue existing components.
- Identify visual debt and inconsistencies.

## Phase 2: Design Tokens
- Codify colors, spacing, type scale, and shadows into a robust token system.
- Ensure the tokens are finalized before touching any actual components.

## Phase 3: Atomic Migration
- Migrate following atomic design principles:
  1. Tokens (variables)
  2. Primitives (icons, typography)
  3. Molecules (buttons, inputs)
  4. Organisms (forms, cards)
  5. Layouts/Pages

## Phase 4: Validation
- Perform a before/after comparison to ensure no functionality was lost.
- Conduct an accessibility audit (contrast, keyboard navigation).
- Perform a performance regression check.
