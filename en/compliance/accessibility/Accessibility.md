# Accessibility

## Overview

Kinana is committed to providing an accessible educational platform that serves all users, including those with disabilities. The platform targets WCAG 2.1 Level AA compliance to ensure inclusive access to educational content.

**Standard**: Web Content Accessibility Guidelines (WCAG) 2.1 Level AA  
**Scope**: All Kinana sub-apps (Shell, Library, Videos, Podcasts, Brokkly)

---

## WCAG 2.1 AA Compliance

### Compliance Framework

**Target Level**: WCAG 2.1 Level AA  
**Current Status**: In implementation (pre-production)  
**Testing**: Ongoing during development

### WCAG Principles (POUR)

#### 1. Perceivable

**Users must be able to perceive information**

**Text Alternatives (Level A)**:

- Alt text for all images
- Captions for videos
- Transcripts for podcasts
- Descriptive link text (no "click here")

**Time-Based Media (Level A, AA)**:

- Closed captions for all video content
- Audio descriptions for video (if needed for comprehension)
- Transcripts for audio content (podcasts)

**Adaptable (Level A)**:

- Semantic HTML structure
- Logical heading hierarchy (H1 → H2 → H3)
- Programmatic relationships (labels with form fields)
- Meaningful sequence maintained on reflow

**Distinguishable (Level AA)**:

- Color contrast ratio 4.5:1 for normal text, 3:1 for large text
- Color not sole means of conveying information
- Audio control (play, pause, volume)
- Resize text up to 200% without loss of functionality
- Images of text avoided (use actual text)

#### 2. Operable

**Users must be able to operate the interface**

**Keyboard Accessible (Level A)**:

- All functionality available via keyboard
- No keyboard traps
- Focus visible and logical
- Tab order follows visual order

**Enough Time (Level A)**:

- Users can extend time limits
- No auto-playing content without control
- Pause, stop, hide options for moving content

**Navigable (Level AA)**:

- Skip navigation links
- Descriptive page titles
- Focus order follows reading order
- Link purpose clear from text or context
- Multiple navigation methods (menu, search, breadcrumbs)
- Clear headings and labels

**Input Modalities (Level A)**:

- Functions available with pointer or keyboard
- Motion actuation alternatives
- Target size adequate (44×44 CSS pixels recommended)

#### 3. Understandable

**Users must be able to understand information and interface**

**Readable (Level A, AA)**:

- Language of page programmatically determined
- Language of parts specified (for mixed-language content)
- Clear, simple language (educational context)

**Predictable (Level A, AA)**:

- Consistent navigation across platform
- Consistent identification of components
- No unexpected context changes
- Consistent Help mechanism

**Input Assistance (Level A, AA)**:

- Error identification and description
- Labels and instructions for forms
- Error suggestions provided
- Error prevention for critical actions (confirmation dialogs)

#### 4. Robust

**Content must work with current and future technologies**

**Compatible (Level A)**:

- Valid HTML/CSS
- ARIA attributes used correctly
- Status messages programmatically determined
- Compatible with assistive technologies

---

## Implementation Standards

### HTML Semantic Structure

```html
<!-- Proper heading hierarchy -->
<h1>Main Page Title</h1>
<h2>Section Title</h2>
<h3>Subsection</h3>

<!-- Semantic landmarks -->
<header role="banner">...</header>
<nav role="navigation" aria-label="Main menu">...</nav>
<main role="main">...</main>
<aside role="complementary">...</aside>
<footer role="contentinfo">...</footer>

<!-- Form accessibility -->
<label for="email">Email Address:</label>
<input
  type="email"
  id="email"
  name="email"
  aria-required="true"
  aria-describedby="email-help"
/>
<span id="email-help">We'll never share your email.</span>

<!-- Button accessibility -->
<button aria-label="Close dialog">×</button>

<!-- Image accessibility -->
<img
  src="diagram.png"
  alt="System architecture showing Shell, Library, Videos, Podcasts, and Brokkly components"
/>
```

### ARIA (Accessible Rich Internet Applications)

**ARIA Usage Principles**:

- Native HTML preferred over ARIA when possible
- ARIA used to enhance semantic meaning
- Dynamic content updates announced to screen readers
- Focus management for modals and overlays

**Common ARIA Patterns**:

```html
<!-- Alerts -->
<div role="alert" aria-live="assertive">
  Error: Please fill in required fields
</div>

<!-- Loading state -->
<div aria-live="polite" aria-busy="true">Loading content...</div>

<!-- Expandable sections -->
<button aria-expanded="false" aria-controls="section1">
  Show more details
</button>
<div id="section1" hidden>...</div>

<!-- Navigation current page -->
<a href="/home" aria-current="page">Home</a>
```

### Color Contrast

**Minimum Ratios (WCAG AA)**:

- Normal text (< 24px): 4.5:1
- Large text (≥ 24px or 18px bold): 3:1
- UI components and graphics: 3:1

**Tools for Verification**:

- Browser DevTools color picker (contrast ratio display)
- WebAIM Contrast Checker: https://webaim.org/resources/contrastchecker/
- Color Contrast Analyzer (desktop tool)

**Kinana Design System**:

- Primary color palette tested for AA compliance
- Accessible color combinations documented
- Designers use contrast checker during design phase

### Keyboard Navigation

**Standard Patterns**:

- Tab: Move to next focusable element
- Shift+Tab: Move to previous focusable element
- Enter/Space: Activate buttons and links
- Arrow keys: Navigate menus and lists
- Escape: Close modals and cancel actions

**Focus Indicators**:

- Visible focus outline (never `outline: none` without alternative)
- Sufficient contrast for focus indicators (3:1 ratio)
- Consistent focus styling across platform

**Skip Links**:

```html
<a href="#main-content" class="skip-link"> Skip to main content </a>
```

### Form Accessibility

**Required Fields**:

- Visual indicator (asterisk)
- Programmatic indicator (aria-required="true")
- Clear in labels (e.g., "Email (required)")

**Error Messages**:

- Associated with form field (aria-describedby)
- Announced to screen readers (aria-live)
- Clear, specific instructions to fix

**Validation**:

- Real-time validation with announcements
- Error summary at top of form
- Focus moved to first error on submission

---

## Testing Procedures

### Manual Testing

#### Keyboard Navigation Testing

**Steps**:

1. Unplug mouse or don't use it
2. Tab through entire page
3. Verify all interactive elements reachable
4. Test keyboard shortcuts and interactions
5. Ensure logical tab order
6. Verify focus indicators visible

**Checklist**:

- ☐ All links and buttons keyboard accessible
- ☐ Forms can be completed without mouse
- ☐ Modals and overlays keyboard operable
- ☐ No keyboard traps
- ☐ Focus indicators clearly visible

#### Visual Testing

**Steps**:

1. Test with browser zoom (up to 200%)
2. Test with different screen resolutions
3. Test responsive design on mobile
4. Verify color contrast
5. Check text spacing adjustments

**Checklist**:

- ☐ Layout doesn't break at 200% zoom
- ☐ No horizontal scrolling on mobile
- ☐ Color contrast meets AA ratios
- ☐ Content reflows appropriately
- ☐ Text remains readable when styled

#### User Testing

**Steps**:

1. Recruit users with disabilities
2. Conduct moderated usability sessions
3. Observe actual usage patterns
4. Gather feedback on pain points
5. Iterate based on findings

**Participants**:

- Users with visual impairments
- Users with motor disabilities
- Users with cognitive disabilities
- Users relying on assistive technologies

---

### Platform-Specific Considerations

#### Library Sub-App (PDF Viewer)

- PDF documents should be accessible (tagged PDFs)
- Provide text alternatives for complex diagrams
- Document structure navigation (headings, bookmarks)

#### Videos Sub-App

- Video player keyboard accessible
- Play/pause, volume, seek controls announced
- Closed captions available
- Video controls properly labeled

#### Podcasts Sub-App

- Audio player keyboard accessible
- Play/pause, volume, seek controls announced
- Transcripts provided for episodes
- Playlist navigation accessible

#### Brokkly (Visual Coding)

- Drag-and-drop alternative (keyboard-based coding)
- Code blocks announced clearly
- Block structure navigable by keyboard
- Visual output described for screen reader users

---

## Accessibility Resources

### Guidelines & Standards

- **WCAG 2.1**: https://www.w3.org/WAI/WCAG21/quickref/
- **ARIA Authoring Practices**: https://www.w3.org/WAI/ARIA/apg/
- **WebAIM**: https://webaim.org/ (articles, tools, training)

### Testing Tools

- **axe DevTools**: https://www.deque.com/axe/devtools/
- **WAVE**: https://wave.webaim.org/
- **Lighthouse**: Built into Chrome DevTools
- **NVDA**: https://www.nvaccess.org/

### Training & Education

- **WebAIM's free courses**: https://webaim.org/training/
- **Microsoft's Inclusive Design**: https://www.microsoft.com/design/inclusive/
- **Google's Web Accessibility course**: https://web.dev/learn/accessibility/

---

## Accessibility Statement

**Published Location**: Kinana platform footer  
**Content**: Summary of:

- Commitment to accessibility
- WCAG 2.1 Level AA target
- Known limitations
- Contact for accessibility issues
- Feedback process

---

## Continuous Improvement

**Process**:

- User feedback monitored and addressed
- Quarterly accessibility reviews
- Annual third-party audit (recommended)
- Stay current with WCAG updates
- Team training on accessibility best practices

**Responsibility**:

- **Solution Architect**: Technical implementation oversight
- **Senior Developer**: Coding accessibility into features
- **Designers**: Accessible design from start
- **QA/PM**: Accessibility testing validation

---

_Last Updated: November 2025_  
_Version: 1.0_  
_Target: WCAG 2.1 Level AA Compliance_
