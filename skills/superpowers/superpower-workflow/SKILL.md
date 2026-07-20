---
name: superpower-workflow
description: Enforces the 7-Phase elite agentic workflow (Brainstorm -> Plan -> TDD -> Draft -> Review -> Refine -> Ship). Use this to ensure high-quality, systematic execution of any feature request.
---

# 7-Phase Agentic Workflow

When tasked with building a feature or completing a complex coding assignment, you MUST follow this 7-Phase Workflow systematically. Do not skip phases.

## Phase 1: Brainstorm
- Analyze the user's request.
- Identify the core problem and constraints.
- Briefly list 2-3 potential approaches before settling on the best one.

## Phase 2: Plan
- Create a step-by-step implementation plan.
- Identify required files, dependencies, and potential side-effects.
- Stop and ask the user for approval if the architectural changes are significant.

## Phase 3: TDD (Test-Driven Development)
- Write the tests for the feature *before* writing the implementation.
- Ensure edge cases and happy paths are covered.

## Phase 4: Draft
- Write the initial implementation of the code.
- Focus on getting the logic correct according to the tests.

## Phase 5: Review
- Perform a self-review of the drafted code.
- Check against performance bottlenecks, security vulnerabilities, and project conventions (e.g., App Router rules, Tailwind utility usage).

## Phase 6: Refine
- Optimize the code based on the Phase 5 review.
- Refactor for readability, DRYness, and modularity.
- Ensure all tests pass.

## Phase 7: Ship
- Finalize the changes.
- Provide a concise summary of what was done.
- Do not over-explain standard patterns. Just deliver the result.
