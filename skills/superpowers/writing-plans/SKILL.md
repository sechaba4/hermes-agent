---
name: writing-plans
description: Structured plan writing format for implementation proposals. Ensures specificity, risk assessment, and rollback strategy. Use when writing plans or proposals for significant changes.
---

# Writing Plans Format

When writing implementation plans or proposals, follow this structure. Ensure that the tone is specific, not vague, and every change includes a "why."

## 1. Problem Statement
Clearly define what the problem is and why it needs to be solved.

## 2. Proposed Changes
Detail the changes file-by-file. Include before/after code snippets where applicable.

## 3. Risk Assessment
Identify what could break as a result of these changes (e.g., unintended side effects on other components, performance impacts).

## 4. Rollback Strategy
Describe the exact steps to revert the changes if things go wrong.

## 5. Testing Plan
Outline the manual verification steps and any automated testing steps that need to be run to confirm the changes work as expected.
