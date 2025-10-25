---
name: product-validation
description: Applies lean startup methodology and user research to validate product assumptions, define MVP scope, and prioritize features based on evidence rather than opinions. Use when defining product requirements, validating features, or analyzing user feedback.
version: 1.0.0
---
<!-- TODO: NEEDS REVIEW! -->
# Product Discovery

Complete product discovery combining lean startup methodology and user research.

## Validated Learning

- Test hypotheses with data, not opinions
- Fail fast and cheaply
- Trust behavior over statements
- When 3+ users mention it → it's a pattern

## MVP Thinking

- Minimum experiment to validate assumptions
- Not a crappy version - strategically minimal
- Build to learn, not just to ship

## Assumptions & Validation

### Assumption Types

| Type | Question | Risk Indicators |
|------|----------|-----------------|
| **Value** | Will customers find this valuable? | Requires behavior change, novel solution |
| **Growth** | Will the product grow? | Unproven acquisition channel |
| **Feasibility** | Can we build this? | Complex tech, regulatory unknowns |

### Hypothesis Format

```markdown
We believe [customer segment] experiences [problem]
and that [solution] will [outcome/benefit].

We will know we're right when [measurable signal].
```

### Pre-Implementation Validation Checklist

- [ ] Riskiest assumptions tested
- [ ] Evidence of customer demand
- [ ] Prototype tested with users
- [ ] Success metrics defined
- [ ] Scope is truly minimal

### Validation Methods (by cost/speed)

| Method | Cost | Duration | Good For | When |
|--------|------|----------|----------|------|
| **Customer Interviews** | Time only | 1-2 weeks | Problem validation | Before anything |
| **Landing Page** | $100-500 | 1-2 days | Demand signals | After problem validation |
| **Mockup Testing** | $200-500 | 3-5 days | UX validation | Before development |
| **Wizard of Oz** | Low upfront | 1-2 weeks | Workflow validation | Before automation |
| **MVF** | High | 1-2 weeks | Real usage | After problem/solution validation |

### Interviews (5-10 users)

**Extract & Prioritize:**

- **Frequency**: How many mentioned it?
- **Intensity**: How painful? ("annoying" vs "deal-breaker")
- **Urgency**: How soon needed?
- **Willingness to Pay**: Would they pay to solve it?
- **Pattern = 3+ users mention unprompted**
- **Prioritize = Frequency × Intensity**

### Risk Assessment

**High Risk = Must Validate:**

- Requires user behavior change
- No proven market
- Complex technology/integration
- Regulatory uncertainty
- Unproven business model

**Questions identifying risks:**

- What must be true for this to work?
- What could cause complete failure?
- Which assumptions have most uncertainty?
- Which, if wrong, would be most costly?

### On each Feature

- Feature goal (problem + value)
- User stories
- UI/UX requirements
- Acceptance criteria
- Identify Assumptions:

   ```markdown
   ## Assumptions to Validate
   - **[Assumption]**
   - Validation: [Method]
   - Success: [Criteria]
   - Priority: HIGH/MEDIUM/LOW
   ```

### On each Update Feature iteration

1. Analyze Changes:
   - Compare with previous product.md
   - Check for new files (feedback, research)
2. Incorporate Research:
   - Extract patterns from feedback/testing
   - Update requirements based on validated learnings
   - Mark assumptions as ✅ validated / ❌ invalidated
   - Adjust acceptance criteria
3. Document:

   ```markdown
   ## Research-Driven Changes
   ### [Activity] (Date)
   - **Finding**: [Learning]
   - **Impact**: [Change]
   - **Updated**: [What changed]
   ```

## MVP Scope Management

**Include:** Core problem solver, minimum value, enables learning, technically feasible

**Defer:** Nice-to-haves, optimizations, secondary segments, features requiring MVP learnings

**Right-size large scope:**

- Which 3-4 criteria validate core hypothesis?
- What's the 20% delivering 80% of learning?

## Pivot or Persevere

| Signal | Action |
|--------|--------|
| Hypothesis disproven | **Pivot** |
| Wrong problem / wrong segment | **Pivot** |
| Can't find acquisition channel | **Pivot** |
| Hypothesis validated | **Persevere** |
| Metrics improving | **Persevere** |
| PMF indicators emerging | **Persevere** |

**Pivot Types:** Zoom-in/out, customer segment, customer need, platform, business model, channel

## Quick Reference Templates

### Interview Insights

```markdown
## User Interview Insights (X participants)

### Key Pain Points
1. **[Pain]** - X/Y mentioned - HIGH/MED/LOW intensity
   - Current solutions: [...]
   - Quote: "[...]"
   - Implication: [...]

### Validated
- ✅ [Confirmed assumption]
- ❌ [Contradicted assumption]
- ⚠️ [Unclear, needs more testing]
```

### Usability Test Results

```markdown
## Usability Test: [Feature] (X users)

🔴 **Critical**: [Issue] - X/Y users - [Fix]
🟡 **Major**: [Issue] - X/Y users - [Fix]
🟢 **Positive**: [What worked]

| Task | Success | Time | Satisfaction |
|------|---------|------|--------------|
| [Task] | 75% | 2:30 | 5.5/7 |
```

### Feedback Analysis

```markdown
## Feedback Analysis: [Period]

### Top Themes
1. **[Theme]** (45% of feedback) - 80% negative
   - [Issue 1] - 23 mentions
   - Action: [...]

### Top Requests
1. [Feature] - X requests - [Segments]
```
