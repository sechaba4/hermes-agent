---
name: design-review
description: Structured design quality review framework. Evaluates spacing, color, typography, animation, and composition with severity ratings and actionable improvement suggestions. Use when reviewing UI changes or evaluating visual quality.
---

# Design Review Framework

Evaluate the design against the following criteria, assigning scores and providing actionable improvement suggestions ordered by impact.

## Review Checklist & Scoring Rubric

Evaluate these aspects out of 10, weighting them as follows:
- **Typography (25%)**: Hierarchy, scale, weight, and correct font choices.
- **Color Harmony (25%)**: Use of design tokens (no raw hex codes), contrast, and adherence to the 60-30-10 rule.
- **Spacing/Rhythm (20%)**: Consistency with the 8pt grid system.
- **Animation Quality (15%)**: Performance (GPU-only properties), easing, and durations.
- **Overall Cohesion & Composition (15%)**: How well the components fit together and follow progressive disclosure.

## Severity Ratings
When identifying issues, classify them as:
- **Critical**: Breaks layout, severe accessibility issues, or off-brand colors.
- **Major**: Inconsistent spacing, wrong type scale, or layout thrashing animations.
- **Minor**: Slight misalignment, subtle timing tweaks.

## Output Format
Produce a structured review with scores for each category, a summary, and an actionable list of improvements ordered by severity.
