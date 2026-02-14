---
name: uiux-design
description: This skill should be used when the user asks to "design UI", "create mockup", or runs /mockup-product, /mockup-feature, or /figma-mockup commands.
---

Professional UI/UX design knowledge for creating beautiful, intuitive, and accessible interfaces.

## Description

Provides design expertise for creating mockups, prototypes, and user interfaces that are both visually appealing and functionally excellent. Applies design principles, usability best practices, and accessibility standards.

## When to Activate

Activate when:

- User runs `/mockup-product`, `/mockup-feature`, or `/figma-mockup`
- Working with HTML mockup files or design assets
- Context involves user interface design, visual design, or user experience
- Creating or reviewing UI prototypes
- User asks about design principles or UX patterns

## Design Principles

As a professional UI/UX designer, based on the application idea and functional specs, think hard how to provide the most intuitive and engaging user experience.

- **Minimalist yet functional**: Prioritize clarity and ease of use
- **Visual hierarchy**: Use well-thought-out hierarchy with soft gradients and generous white space
- **Intuitive UX**: Provide the most engaging and intuitive user experience
- **Micro-interactions**: Include delicate, frictionless micro-interactions
- **Accessibility**: Stick to WCAG AA principles

### Common UI Patterns

Apply when appropriate.

**Common Best Practices**:

- Use modern CSS (flexbox, grid, custom properties, animations)
- Tailwind CSS (via CDN) for utility classes
- JavaScript for interactions (embedded in `<script>` tags)
- Shadcn UI components (via CDN) when appropriate
- Add hover states, transitions, and subtle animations
- For mockups use realistic placeholder content that demonstrates the interface

**Navigation:**

- Top navigation for few items (3-7 links)
- Sidebar navigation for many items or hierarchy
- Bottom tab bar for mobile (3-5 primary actions)
- Hamburger menu as last resort (hide complexity)

**Forms:**

- One column layout for forms
- Clear labels above inputs
- Helpful placeholder text (not as labels)
- Inline validation with helpful error messages
- Clear primary action button
- Auto-focus first field

**Lists and Cards:**

- Card-based design for browsing and scanning
- List view for dense information
- Grid for visual content (images, products)
- Infinite scroll or pagination based on content type

**Feedback:**

- Toast notifications for transient feedback
- Modal dialogs for critical confirmations
- Inline messages for contextual feedback
- Loading skeletons for content loading
- Empty states with helpful guidance

### Mobile-First Patterns

- Stack vertically on mobile
- Larger touch targets (min 44x44px)
- Bottom sheets for actions on mobile
- Swipe gestures where appropriate
- Fixed position CTAs at bottom of mobile screens

Focus on visual and interaction design - let other skills handle their domains.
