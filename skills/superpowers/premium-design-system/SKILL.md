---
name: premium-design-system
description: Premium visual design system for Term Tracker v2. Covers brand palette, typography, spacing, glassmorphism, gradients, shadows, and luxury-tier execution patterns. Use when creating or modifying UI components.
---

# Premium Design System

## Brand Palette
- **Background**: #0A0A0A
- **Surface**: #141414
- **Gold**: #C9A96E
- **Cream**: #E8D5B7
- **Rose**: #B8707A
- Use the 60-30-10 color rule for balancing the primary, secondary, and accent colors.

## Typography
- **Headings**: Playfair Display
- **Body**: Inter
- **Fluid Type**: `clamp(0.875rem, 0.8rem + 0.4vw, 1.125rem)`
- **Scale**: Modular type scale of 1.25

## Layout & Spacing
- **Base Grid**: 8pt spacing system following golden-ratio principles.
- **Border-radius**: 12-16px
- **Elevation**: 4-level elevation system (e.g., 0/2/8/16px shadows).
- Utilize progressive disclosure patterns to avoid overwhelming users with UI.

## Premium Execution Patterns
- **Glassmorphism**: `backdrop-filter: blur(20px) saturate(180%)`, `background: rgba(255,255,255,0.05)`
- **Gradients**: Create gradient mesh via layered radial-gradient
- **Shadows**: `box-shadow: 0 8px 32px rgba(0,0,0,0.4)`
- **Borders**: `1px solid rgba(255,255,255,0.06)`

## Motion
- **Hover Transitions**: 200ms ease.
