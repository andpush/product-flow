---
name: ui-ux-design
description: Professional UI/UX design expertise for mockups and accessible interfaces
version: 1.0.0
---

# UI/UX Design Expertise

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

### Visual Design

**Minimalist Yet Functional:**
- Prioritize clarity and ease of use
- Remove unnecessary elements
- Every element should serve a purpose
- "Perfection is achieved not when there is nothing more to add, but when there is nothing left to take away"

**Visual Hierarchy:**
- Well-thought-out hierarchy with clear focal points
- Use size, color, contrast, and spacing to guide attention
- Most important actions should be visually dominant
- Progressive disclosure for complex interfaces

**Soft and Calm Aesthetics:**
- Generous white space creates breathing room
- Soft gradients instead of harsh transitions
- Subtle shadows and rounded corners
- Muted color palettes with intentional pops of color
- Typography with good readability and spacing

**Micro-Interactions:**
- Delicate, frictionless micro-interactions
- Hover states that provide subtle feedback
- Smooth transitions and animations (200-300ms)
- Loading states and progress indicators
- Confirmation feedback for user actions

### Interaction Design

**Intuitive UX:**
- Provide the most engaging and intuitive user experience
- Follow established patterns users already know
- Clear affordances (buttons look clickable, inputs look editable)
- Minimize cognitive load
- Progressive enhancement

**Core Actions Prominent:**
- Visually dominant call-to-action buttons
- Primary actions should stand out
- Secondary actions should be visible but less prominent
- Destructive actions require confirmation

**Responsive and Adaptive:**
- Mobile-first approach
- Responsive across all screen sizes
- Touch-friendly tap targets (min 44x44px)
- Appropriate information density for each device

### Accessibility

**WCAG AA Compliance:**
- Color contrast ratios (4.5:1 for text, 3:1 for UI elements)
- All interactive elements keyboard accessible
- Proper focus indicators
- Screen reader compatible (semantic HTML, ARIA labels)
- Alt text for images
- Form labels and error messages
- Don't rely on color alone to convey information

**Inclusive Design:**
- Consider users with different abilities
- Support keyboard navigation
- Provide text alternatives for non-text content
- Ensure readability (font size, line height, contrast)

## Design Thinking Process

Before creating any mockup, think through:

### 1. User Understanding
- **User personas**: Who will use this interface?
- **User goals**: What are they trying to accomplish?
- **Context of use**: Where and how will they use it?
- **Pain points**: What frustrates users in similar interfaces?

### 2. Primary User Flows
- **Critical paths**: Most important user journeys
- **Entry points**: How do users arrive at this screen?
- **Exit points**: Where do they go next?
- **Happy path**: Ideal user journey
- **Edge cases**: Error states, empty states, loading states

### 3. Information Architecture
- **Content hierarchy**: What's most important?
- **Grouping**: How should information be organized?
- **Navigation**: How do users move between sections?
- **Progressive disclosure**: What to show vs hide initially?

### 4. Visual Design Strategy
- **Focal points**: Where should eyes go first?
- **Visual flow**: How should attention move across the page?
- **Emotional tone**: What feeling should the design evoke?
- **Brand alignment**: Does it match product identity?

## Design Process

### Step 1: Gather Requirements

**For Product/Feature Mockups:**
- Read `{{PRODUCT_MD}}` for product context and UI requirements
- Read feature's `feature.md` for specific functionality
- Check `{{UI_REFERENCE}}/` for design systems, style guides, reference designs
- Look for specified design system or branding guidelines

**For Figma-Based Mockups:**
- Extract design from Figma using MCP tools
- Download all assets (images, icons, graphics)
- Extract design tokens (colors, typography, spacing)
- Read `{{PRODUCT_MD}}` for business context
- Follow Figma design unless user explicitly requests changes

### Step 2: Design Thinking

**Think deeply about the user experience:**
- Who is the user and what are they trying to do?
- What's the most intuitive way to accomplish their goal?
- What information do they need at each step?
- How can we make it delightful, not just functional?

**Remember**: You're not just coding a page, you're crafting an experience that should be beautiful, intuitive, and delightful.

### Step 3: Create Mockup

**Technical Implementation:**
- Use Tailwind CSS via CDN for utility classes
- Embed CSS in `<style>` tags
- Embed JavaScript in `<script>` tags for interactions
- Use inline SVGs or base64-encoded images for icons
- Reference external images with relative paths for Figma assets
- Use modern CSS (flexbox, grid, custom properties, animations)
- Add hover states, transitions, and subtle animations

**Component Libraries:**
- Shadcn UI components (via CDN) when appropriate
- Custom components when needed for unique designs
- Ensure components are accessible and semantic

**Content:**
- Use realistic placeholder content
- Demonstrate the interface with real-world examples
- Include different states (empty, loading, error, success)

### Step 4: Quality Assurance

Before completing, verify:
- [ ] Opens correctly in browser
- [ ] Responsive across mobile, tablet, and desktop breakpoints
- [ ] All interactive elements function properly
- [ ] Contains realistic, appropriate mock data
- [ ] Follows accessibility best practices (WCAG AA)
- [ ] Matches feature requirements and user stories
- [ ] Maintains consistent visual design throughout
- [ ] Smooth animations and transitions
- [ ] Good performance (loads quickly, no jank)

## Design Patterns

### Common UI Patterns

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

## Output Formats

### Self-Contained HTML (Default)
- Single HTML file with embedded CSS and JS
- Inline or base64-encoded images
- CDN resources (Tailwind, fonts)
- Saved to `{{MOCKUPS}}/[name].html`

### HTML with Assets (Figma-based)
- Main HTML file: `outputs/mockups/[name].html`
- Assets folder: `outputs/mockups/[name]-assets/`
  - `images/` - Downloaded images, screenshots, icons
  - `styles/` - Design tokens (optional)
- HTML uses relative paths to assets

## Instructions

When this skill is active:

1. **Apply Design Thinking**: Always think through user needs, flows, and information architecture before creating mockups

2. **Follow Design Principles**: Apply minimalist, functional design with good visual hierarchy and accessibility

3. **Create Beautiful Interfaces**: Don't just make it work - make it delightful, intuitive, and visually appealing

4. **Ensure Accessibility**: Every design must meet WCAG AA standards

5. **Use Realistic Content**: Show the interface with real-world examples, not "Lorem ipsum"

6. **Iterate Based on Feedback**: If user provides feedback, refine the design accordingly

7. **Document Design Decisions**: Explain key design choices when presenting mockups

## Integration with Other Skills

- **product-flow-core**: Provides path resolution and workflow context
- **business-analysis**: Provides feature requirements and user stories
- **lean-startup**: Informs what to test and validate in early mockups
- **product-research**: Incorporates user feedback into design iterations

Focus on visual and interaction design - let other skills handle their domains.
