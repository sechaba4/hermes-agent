---
name: superpower-reviewer
description: Acts as an autonomous code reviewer that verifies generated code against best practices, performance metrics, and security guidelines before finalizing output.
---

# Autonomous Code Reviewer

Before presenting code to the user or committing changes, you must put on the "Code Reviewer" hat and audit your own work. 

## The Audit Checklist

### 1. Performance & Rendering
- **React/Next.js**: Are there unnecessary re-renders? Are `useMemo` or `useCallback` needed? 
- Is the `'use client'` directive pushed as far down the component tree as possible?
- Are images optimized? Are heavy components lazy-loaded via `next/dynamic`?

### 2. Security & Data Fetching
- Are Server Actions properly validating input?
- Is RLS (Row Level Security) respected when accessing Supabase?
- Are secrets kept strictly on the server side?

### 3. Maintainability & Style
- Does the code adhere to the project's design system (e.g., Tailwind utilities, CSS variables)?
- Is there any dead code, unused imports, or excessive console.logs?
- Are types strictly defined (no `any`)?

## Review Output
If the audit fails on any point, fix the code internally *before* showing it to the user. 
If the code passes, output a single line: `> Code Review: PASSED` at the end of your response.
