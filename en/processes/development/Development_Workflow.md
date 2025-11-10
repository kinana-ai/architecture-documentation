# Development Workflow

## Overview

Kinana follows an Agile development methodology with 2-week sprint cycles. All development work is tracked in GitHub Projects using a Kanban board structure.

## Sprint Cycle

```
Sprint Planning → Daily Development → Sprint Review → Retrospective
     ↓                    ↓                 ↓              ↓
  2 weeks            Daily standups    Demo & feedback   Improve
```

---

## Sprint Planning

**Frequency**: Bi-monthly (every 2 weeks)  
**Duration**: 1-2 hours  
**Participants**: Full team

### Purpose

Prioritize and commit to work for the upcoming sprint based on product roadmap and technical requirements.

### Process

1. **Backlog Review**

   - Product Manager presents prioritized features and technical debt items
   - Solution Architect identifies technical dependencies and architectural considerations

2. **Task Breakdown**

   - Team collaboratively breaks down features into implementable tasks
   - Tasks are created as GitHub Issues with appropriate labels
   - Effort estimation (optional, team uses experience-based sizing)

3. **Sprint Commitment**

   - Team commits to sprint backlog based on capacity
   - Tasks moved to "Sprint Backlog" column in GitHub Projects

4. **Technical Alignment**
   - Solution Architect provides architectural guidance for complex features
   - Team discusses implementation approaches for high-risk items

### Outputs

- Sprint backlog in GitHub Projects
- Architectural decisions documented in relevant repos
- Clear understanding of sprint goals

---

## Daily Standup

**Frequency**: Daily  
**Duration**: 15 minutes  
**Format**: Synchronous (video/in-person)

### Purpose

Coordinate daily activities, identify blockers, and agree on deployment timing.

### Format

Each team member shares:

1. **Completed**: What was finished since last standup
2. **In Progress**: Current focus
3. **Blockers**: Any impediments to progress

### Key Topics

- **Deployment Coordination**: Agreement on what's ready to push to staging
- **Issue Resolution**: Quick problem-solving or escalation
- **Dependencies**: Cross-component coordination
- **Technical Questions**: Quick architectural clarifications

### Deployment Agreement Protocol

Before pushing to staging:

1. Developer confirms local testing complete
2. Code walkthrough completed (if significant changes)
3. Solution Architect approves merge (for architectural impact)
4. Team consensus on deployment timing

---

## Sprint Review

**Frequency**: End of each sprint (bi-monthly)  
**Duration**: 1 hour or as needed
**Participants**: Full team + stakeholders (as needed)

### Purpose

Demonstrate completed work and gather feedback on implemented features.

### Agenda

1. **Sprint Goal Review** (5 min)

   - Recap sprint objectives
   - Overview of completed vs. planned work

2. **Feature Demonstrations** (40 min)

   - Live demos of completed features in staging environment
   - Each developer demos their contributions
   - Focus on user-facing functionality and technical achievements

3. **Stakeholder Feedback** (15 min)
   - Open discussion on demonstrated features
   - Capture feedback as new GitHub Issues
   - Identify acceptance criteria adjustments

### Demonstration Environment

- **Primary**: Staging environment
- **Fallback**: Local development instances (if staging issues)

### Outputs

- Accepted features (moved to "Done" in GitHub Projects)
- New issues for feedback-driven adjustments
- Updated product backlog priorities

---

## Retrospective

**Frequency**: End of each sprint (bi-monthly)  
**Duration**: 45 minutes  
**Participants**: Development team (internal)

### Purpose

Reflect on process effectiveness and identify improvements for the next sprint.

### Format

Team discusses three categories:

1. **What Went Well** 🟢

   - Celebrate successes and effective practices
   - Identify patterns to reinforce

2. **What Didn't Go Well** 🔴

   - Surface friction points and challenges
   - Discuss root causes without blame

3. **Action Items** 🔵
   - Concrete improvements for next sprint
   - Assign owners for process changes

### Focus Areas

- Development workflow efficiency
- Code review process
- Deployment and testing procedures
- Technical debt management
- Tool and infrastructure improvements
- Team collaboration and communication

### Action Item Tracking

- Action items documented in GitHub Project notes
- Reviewed at start of next retrospective
- Solution Architect or PM owns follow-up

### Continuous Improvement

Process changes are implemented incrementally. Major workflow adjustments require team consensus and documentation updates.

---

## GitHub Projects Workflow

### Board Columns

1. **Backlog**: Prioritized but not committed
2. **Sprint Backlog**: Committed for current sprint
3. **In Progress**: Actively being worked on
4. **Review**: Code complete, awaiting review
5. **Testing**: QA validation in staging
6. **Done**: Accepted and deployed

### Issue Management

- **Labels**: Feature, Bug, Technical Debt, Documentation
- **Assignees**: Developer responsible for implementation
- **Milestones**: Sprint identifier (Sprint 1, Sprint 2, etc.)
- **Projects**: Linked to Kinana Kanban board

### Task Movement

Developers are responsible for moving their tasks through the board as work progresses. QA/PM monitors flow and identifies bottlenecks.

---

## Development Environment Workflow

### Local Development

1. Pull latest from `dev` branch
2. Create feature branch: `feature/description` or `bugfix/description`
3. Implement and test locally
4. Code walkthrough with team (for significant changes)

### Staging Deployment

1. Merge feature branch to `dev` after code review
2. Automated deployment to staging environment
3. QA testing and validation
4. Issues reported back to GitHub

### Testing Protocol

- Developer validates locally before push
- QA validates in staging environment
- Critical bugs block further deployments until resolved

---

_Last Updated: November 2025_  
_Version: 1.0_
