---
name: superpower-planner
description: Forces the agent into 'Plan Mode' to decompose complex problems, map dependencies, and define success criteria BEFORE writing any code.
---

# The Planning Protocol

Before executing any complex feature request, bug fix, or architectural change, you MUST initiate this Planning Protocol.

## The Contract
Define the following four elements clearly in a brief markdown block:

1. **Role**: What specialized persona is required for this task? (e.g., "Postgres DBA", "React Performance Expert").
2. **Goal**: What is the verifiable definition of success? How will we know it's done?
3. **Constraints**: What must be avoided? (e.g., "Do not add new npm packages", "Must remain backwards compatible with v1 API").
4. **Verification**: How will the solution be tested? (e.g., "Run specific Playwright test", "Check React devtools for re-renders").

## Execution Steps
1. Map out the dependencies: Which files will be touched? How does this affect the database schema?
2. Write a sequential list of steps.
3. Pause for user review if the plan involves sweeping changes, database migrations, or new infrastructure.
4. Execute the steps sequentially, crossing them off as they are completed.
