# Version Control Standards

## Overview

Kinana uses Git with GitHub Enterprise for version control across 22 repositories. These standards ensure consistent workflow, clear history, and effective collaboration.

**Reference**: [Conventional Commits](https://www.conventionalcommits.org/) for commit messages

---

## Git Workflow

### Development Flow

```
1. Clone repository
2. Create feature branch from 'dev'
3. Develop and commit locally
4. Push feature branch to GitHub
5. Create Pull Request
6. Code review and approval
7. Merge to 'dev'
8. Deploy to staging (automated)
9. QA testing in staging
```

**Current Branches**:

- `dev`: Active development branch (primary)
- `feature/*`: Feature development branches
- `bugfix/*`: Bug fix branches
- `main` / `production`: Not yet in use (future production)

---

## Branching Strategy

### Branch Types

**Development Branch** (`dev`):

- Main working branch
- All features merge here
- Deploys to staging environment
- Protected: requires PR and approval

**Feature Branches** (`feature/`):

```bash
# Pattern: feature/issue-number-brief-description
feature/123-add-pdf-viewer
feature/456-implement-arabic-rtl
feature/789-user-authentication

# Create from dev
git checkout dev
git pull origin dev
git checkout -b feature/123-add-pdf-viewer
```

**Bug Fix Branches** (`bugfix/`):

```bash
# Pattern: bugfix/issue-number-brief-description
bugfix/234-fix-login-redirect
bugfix/567-pdf-rendering-issue

# Create from dev
git checkout dev
git pull origin dev
git checkout -b bugfix/234-fix-login-redirect
```

**Hotfix Branches** (future, for production):

```bash
# Pattern: hotfix/version-description
hotfix/1.0.1-critical-security-fix

# Create from main/production
git checkout main
git pull origin main
git checkout -b hotfix/1.0.1-critical-security-fix
```

### Branch Naming Rules

- Use lowercase kebab-case
- Include issue/ticket number when applicable
- Be descriptive but concise
- No special characters except hyphens

---

## Commit Messages

### Format (Conventional Commits)

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Type

- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation changes
- **style**: Code style changes (formatting, no logic change)
- **refactor**: Code refactoring (no feature/fix)
- **perf**: Performance improvement
- **test**: Adding or updating tests
- **chore**: Build process, dependencies, tooling

### Examples

**Good Commits**:

```bash
# Feature
git commit -m "feat(library): add PDF text extraction

Implement text extraction using GDPicture library.
Supports Arabic and English text.

Closes #123"

# Bug fix
git commit -m "fix(auth): resolve token expiration issue

Users were being logged out prematurely due to incorrect
token expiration calculation.

Fixes #456"

# Documentation
git commit -m "docs(readme): update installation instructions"

# Refactor
git commit -m "refactor(user-service): simplify query logic"

# Style
git commit -m "style(components): format with Prettier"

# Chore
git commit -m "chore(deps): upgrade Angular to v17"
```

**Bad Commits**:

```bash
# ❌ Too vague
git commit -m "fix bug"
git commit -m "update code"
git commit -m "changes"

# ❌ No context
git commit -m "fix"

# ❌ Multiple unrelated changes
git commit -m "add feature, fix bug, update docs"
```

### Commit Best Practices

**Atomic Commits**:

- One logical change per commit
- Should be buildable and testable
- Easy to review and revert if needed

```bash
# ✅ Good - separate commits
git commit -m "feat(library): add document upload"
git commit -m "feat(library): add document preview"
git commit -m "test(library): add upload tests"

# ❌ Bad - one huge commit
git commit -m "add entire library feature"
```

**Commit Frequency**:

- Commit often (daily at minimum)
- Push to remote regularly (backup and visibility)
- Don't wait until feature is "perfect"

---

## Pull Request Guidelines

### Creating Pull Requests

**PR Title**: Should follow commit message format

```
feat(library): add PDF viewer component
fix(auth): resolve login redirect issue
docs(api): update endpoint documentation
```

**PR Description Template**:

```markdown
## Description

Brief description of changes and motivation.

## Related Issue

Closes #123
Relates to #456

## Type of Change

- [ ] Bug fix (non-breaking change fixing an issue)
- [ ] New feature (non-breaking change adding functionality)
- [ ] Breaking change (fix or feature causing existing functionality to change)
- [ ] Documentation update

## Changes Made

- Detailed list of changes
- Key implementation decisions
- Any trade-offs made

## Testing Performed

- Local testing steps
- Edge cases tested
- Browser/device testing (if UI)

## Screenshots (if applicable)

[Add screenshots for UI changes]

## Checklist

- [ ] Code follows project style guidelines
- [ ] Self-review completed
- [ ] Code commented where needed
- [ ] Documentation updated
- [ ] No new warnings generated
- [ ] Tested locally
```

### PR Size

- **Small PRs preferred**: < 400 lines changed
- **Maximum**: < 1000 lines (break into multiple PRs if larger)
- **Exception**: Generated code, migrations, package updates

### Draft PRs

- Use draft PRs for work-in-progress
- Get early feedback on approach
- Convert to ready when complete

---

## Code Review Process

### Review Assignment

- **Default**: Solution Architect reviews all PRs
- **Peer Review**: Encouraged before architect review
- **Self-Assignment**: Don't approve your own PRs

### Review Checklist

See separate [Code Review Checklist](./Version_Control_Code_Review_Checklist.md)

Quick checklist:

- [ ] Code implements stated requirements
- [ ] No obvious bugs or logic errors
- [ ] Follows coding standards
- [ ] Error handling present
- [ ] Security considerations addressed
- [ ] Performance acceptable
- [ ] Tests included (when testing implemented)

### Review Feedback

**Giving Feedback**:

```markdown
# ✅ Good - constructive, specific

This could cause a memory leak because the subscription isn't unsubscribed.
Consider using `takeUntil(destroy$)` pattern.

# ✅ Good - asks questions

Why did you choose this approach over using the built-in method?

# ✅ Good - suggests improvement

Consider extracting this logic into a separate function for reusability.

# ❌ Bad - not constructive

This is wrong.

# ❌ Bad - too vague

Clean this up.
```

**Receiving Feedback**:

- Don't take it personally
- Ask for clarification if needed
- Respond to all comments (even if just "fixed")
- Mark conversations as resolved when addressed

### Approval and Merge

**Approval Requirements**:

- Solution Architect approval required
- Passing CI checks (when implemented)
- No unresolved conversations

**Merge Methods**:

- **Squash and Merge** (preferred for feature branches)
  - Creates single commit in dev
  - Keeps history clean
  - Preserves PR number in commit

```bash
# Squash merge result
feat(library): add PDF viewer (#123)

* Multiple commits get squashed
* PR description preserved
* Issue references maintained
```

- **Regular Merge** (for release branches, future)
  - Preserves all commits
  - Shows full development history

---

## Repository Cloning

### Using GitHub CLI

```bash
# Clone Kinana repository
gh repo clone kinana-ai/ai.kinana.common
cd ai.kinana.common
```

### Using Git

```bash
# Clone with SSH (preferred)
git clone git@github.com:kinana-ai/ai.kinana.common.git
cd ai.kinana.common

# Clone with HTTPS
git clone https://github.com/kinana-ai/ai.kinana.common.git
```

### Initial Setup

```bash
# Configure user (if not done globally)
git config user.name "Your Name"
git config user.email "your.email@ibtikaredutech.com"

# Set up remote tracking
git branch --set-upstream-to=origin/dev dev
```

---

## Common Git Commands

### Daily Workflow

```bash
# Start work
git checkout dev
git pull origin dev
git checkout -b feature/123-new-feature

# Make changes, commit
git add .
git commit -m "feat(component): add new feature"

# Push to remote
git push origin feature/123-new-feature

# Create PR on GitHub (or via gh CLI)
gh pr create --title "feat(component): add new feature" --body "Description"

# After approval, update your local dev
git checkout dev
git pull origin dev
```

### Syncing with Remote

```bash
# Update your feature branch with latest dev
git checkout feature/123-my-feature
git fetch origin
git rebase origin/dev  # Or merge if you prefer

# Resolve conflicts if any
git add <resolved-files>
git rebase --continue

# Force push (since rebased)
git push origin feature/123-my-feature --force-with-lease
```

### Undoing Changes

```bash
# Undo uncommitted changes
git checkout -- <file>
git restore <file>  # Git 2.23+

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Undo last commit (discard changes)
git reset --hard HEAD~1

# Amend last commit
git commit --amend -m "New message"
```

---

## Multi-Repository Coordination

### Kinana Architecture (22 Repositories)

**Challenge**: Changes often span multiple repos

**Coordination**:

- Document cross-repo dependencies in PR description
- Link related PRs with "Depends on #PR-number in repo-name"
- Coordinate merge timing in daily standup
- Test integrated system in staging

**Example**:

```markdown
## Related Changes

This PR depends on:

- kinana-ai/shell-app#456 (API contract change)
- kinana-ai/common-lib#789 (shared model update)

Merge order: common-lib → shell-app → this PR
```

---

## Git Hygiene

### Keep Branches Clean

```bash
# Delete merged local branches
git branch --merged | grep -v "dev" | xargs git branch -d

# Delete remote-tracking branches that no longer exist
git fetch --prune

# List stale branches
git branch -vv | grep ': gone]'
```

### .gitignore Best Practices

```
# Always ignore
node_modules/
dist/
build/
.env
.env.local
*.log

# IDE
.vscode/
.idea/
*.swp

# OS
.DS_Store
Thumbs.db

# Never ignore
!.gitkeep (for empty directories)
```

---

## Git Configuration

### Recommended Settings

```bash
# Use main as default branch name
git config --global init.defaultBranch main

# Colorful diff
git config --global color.ui auto

# Set default editor
git config --global core.editor "code --wait"

# Rebase on pull
git config --global pull.rebase true

# Auto-stash when rebasing
git config --global rebase.autoStash true

# Push current branch by default
git config --global push.default current
```

---

## Resources

- **Conventional Commits**: https://www.conventionalcommits.org/
- **GitHub Flow**: https://docs.github.com/en/get-started/quickstart/github-flow
- **Pro Git Book**: https://git-scm.com/book/en/v2
- **GitHub CLI**: https://cli.github.com/

---

_Last Updated: November 2025_  
_Version: 1.0_
