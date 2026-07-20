---
name: animation-review
description: Animation quality review guidelines. Checks for 60fps performance, accessibility, meaningful transitions, and spring physics. Use when creating, reviewing, or modifying animations and transitions.
---

# Animation Review Guidelines

## Core Principles
- **Performance**: Must run at 60fps. Use only GPU-accelerated properties (transform, opacity).
- **Accessibility**: Respect `prefers-reduced-motion` mandatory.
- **Purpose**: Meaningful transitions, avoid gratuitous animations.
- **Physics**: Use spring physics for an organic feel (defaults: tension 170, friction 26).

## Motion Choreography
- **Micro-interactions**: 150ms
- **Layout Transitions**: 300ms
- **Easing**: `cubic-bezier(0.4, 0, 0.2, 1)`
- **Stagger**: 50ms delay between siblings.

## Duration Limits
- **Micro**: 100-200ms
- **Macro**: 250-400ms
- **Page Transitions**: 400-600ms

## Restrictions
- **No Animation on Layout Properties**: Never animate `width`, `height`, `top`, `left`, etc. as they trigger layout recalculations.
