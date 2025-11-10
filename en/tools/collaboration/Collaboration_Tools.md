# Collaboration Tools

## Overview

The Kinana team uses GitHub for project management and version control, Microsoft Teams for communication and meetings, and Azure for staging infrastructure access.

**Note**: Team does **not** use Azure DevOps or Jira. All project management occurs through GitHub Projects.

---

## GitHub Projects

### Overview

**Purpose**: Agile project management using Kanban methodology  
**Access**: All team members have access to project board  
**Integration**: Linked directly to code repositories for seamless workflow

### Project Board Structure

#### Board Columns

| Column             | Purpose                                 | Who Moves Items                  |
| ------------------ | --------------------------------------- | -------------------------------- |
| **Backlog**        | Prioritized but not committed to sprint | Product Manager                  |
| **Sprint Backlog** | Committed for current 2-week sprint     | Team during sprint planning      |
| **In Progress**    | Actively being worked on                | Developer assigned to task       |
| **Review**         | Code complete, awaiting review          | Developer after PR submission    |
| **Testing**        | QA validation in staging                | QA/PM after code review approval |
| **Done**           | Accepted and deployed                   | QA/PM after validation           |

#### Automation Rules

- Issue created → Automatically added to Backlog
- PR opened → Linked issue moves to Review
- PR merged → Linked issue moves to Testing
- Issue closed → Moves to Done

### Issue Management

#### Issue Types (Labels)

- `feature`: New functionality
- `bug`: Defects or incorrect behavior
- `technical-debt`: Code quality improvements
- `documentation`: Documentation updates
- `enhancement`: Improvements to existing features

#### Priority Labels

- `priority-critical`: Blocking issues, immediate attention
- `priority-high`: Important for current sprint
- `priority-medium`: Nice to have in sprint
- `priority-low`: Future consideration

#### Component Labels

- `shell`: Core application
- `library`: Document management
- `videos`: Video platform
- `podcasts`: Podcast platform
- `brokkly`: Visual coding
- `infrastructure`: Azure/Kubernetes/Docker

#### Issue Template

When creating issues, include:

```markdown
## Description

Clear description of the feature or bug

## Acceptance Criteria

- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

## Technical Notes

Any architectural considerations or dependencies

## Related Issues

Link to related issues or PRs

## Estimated Effort (optional)

Team uses experience-based sizing
```

### Sprint Management

#### Milestones

Each 2-week sprint has a milestone:

- **Name**: `Sprint N` (e.g., Sprint 23)
- **Due Date**: End of sprint
- **Description**: Sprint goals and objectives

Issues are tagged with milestone during sprint planning.

### Pull Request Workflow

#### Linking to Issues

**Required**: Every PR must reference an issue

```markdown
Closes #123
```

This automatically:

- Links PR to issue
- Moves issue to Review when PR opened
- Closes issue when PR merged

#### PR Labels

- `needs-review`: Awaiting code review
- `changes-requested`: Reviewer requested modifications
- `approved`: Ready to merge
- `wip`: Work in progress, not ready for review

### Project Views

**Default View**: Kanban board (primary workflow)

**Additional Views**:

- **Sprint View**: Filter by current sprint milestone
- **By Component**: Group issues by component labels
- **By Assignee**: See each team member's workload
- **Roadmap**: Timeline view of milestones

### Team Workflow

#### Daily Standup Integration

Each team member references:

- Issues currently "In Progress"
- Issues moved to "Review" since last standup
- Blockers (issues with `blocked` label)

#### Sprint Planning Integration

1. Product Manager prioritizes Backlog
2. Team reviews top items
3. Items moved to "Sprint Backlog" during commitment
4. Issues tagged with sprint milestone

#### Sprint Review Integration

- Demo issues in "Testing" or "Done"
- Stakeholders provide feedback (captured as new issues)
- Accepted items moved to "Done"

---

## Azure Infrastructure Access

### Overview

**Access**: Solution Architect and Senior Developer only  
**Purpose**: Staging environment management, deployment monitoring, troubleshooting

### Azure Portal

**URL**: [portal.azure.com](https://portal.azure.com)

**Authentication**: YHT corporate Azure AD accounts

**Key Resources**:

- **Resource Group**: `kinana-staging`
- **AKS Cluster**: `kinana-aks-staging`
- **Container Registry**: `kinanacr.azurecr.io`
- **Storage Accounts**: Various for sub-app data
- **Application Insights**: Monitoring and logging

### Azure CLI

**Installation**:

```bash
# Windows
winget install Microsoft.AzureCLI

# macOS
brew install azure-cli
```

**Common Commands**:

```bash
# Login
az login

# Get AKS credentials
az aks get-credentials --resource-group kinana-staging --name kinana-aks-staging

# List resources
az resource list --resource-group kinana-staging

# View container registry
az acr repository list --name kinanacr
```

### Kubernetes (kubectl)

**Installation**:

```bash
# Via Azure CLI
az aks install-cli

# Or direct download
# https://kubernetes.io/docs/tasks/tools/
```

**Configuration**:

```bash
# Get staging cluster credentials
az aks get-credentials --resource-group kinana-staging --name kinana-aks-staging --overwrite-existing
```

**Common Operations**:

```bash
# View all pods
kubectl get pods --all-namespaces

# View specific service
kubectl get pods -n kinana-shell

# View logs
kubectl logs pod-name -n kinana-shell

# Describe pod for troubleshooting
kubectl describe pod pod-name -n kinana-shell

# Execute command in pod
kubectl exec -it pod-name -n kinana-shell -- /bin/bash

# Port forwarding for local debugging
kubectl port-forward pod-name 5000:5000 -n kinana-shell
```

**Deployment Verification**:

```bash
# Check deployment status
kubectl rollout status deployment/kinana-shell -n kinana-shell

# View deployment history
kubectl rollout history deployment/kinana-shell -n kinana-shell

# Rollback if needed
kubectl rollout undo deployment/kinana-shell -n kinana-shell
```

### Monitoring & Logging

**Application Insights**:

- Access via Azure Portal
- View application performance metrics
- Query logs with Kusto Query Language (KQL)
- Set up alerts for critical errors

**Log Analytics**:

```bash
# View logs in portal or via CLI
az monitor log-analytics query \
  --workspace [WORKSPACE_ID] \
  --analytics-query "ContainerLog | where TimeGenerated > ago(1h)"
```

### Access Control

**Role-Based Access**:

- Solution Architect: Owner permissions on staging resource group
- Senior Developer: Contributor permissions on staging resource group

**Security Best Practices**:

- Use Azure CLI login (no hardcoded credentials)
- kubectl config tied to Azure AD authentication
- Access reviewed quarterly

---

## Microsoft Teams

### Overview

**Instance**: YHT Corporate Microsoft Teams  
**Purpose**: Real-time communication, meetings, and collaboration

### Team Structure

**Kinana Development Team** (Team name in Teams)

**Channels**:

- **General**: Announcements, team-wide communication
- **Daily Standup**: Quick updates and coordination
- **Development**: Technical discussions, code questions
- **Deployment**: Staging deployment notifications and coordination
- **QA & Testing**: Bug reports, testing coordination
- **Documentation**: Links to docs, PRD reviews

### Meeting Types

#### Daily Standup

- **Schedule**: Every working day, 15 minutes
- **Format**: In person or Video call
- **Recording**: Not required (brief updates)
- **Attendees**: Full team

#### Sprint Planning

- **Schedule**: Bi-monthly, start of sprint
- **Duration**: 1-2 hours
- **Format**: In person or Video call with screen sharing
- **Recording**: Not required (brief updates)
- **Attendees**: Full team

#### Sprint Review

- **Schedule**: End of sprint
- **Duration**: 1 hour
- **Format**: Live demo in staging environment
- **Recording**: Recommended (for stakeholders who can't attend)
- **Attendees**: Team + stakeholders

#### Retrospective

- **Schedule**: End of sprint
- **Duration**: 45 minutes
- **Format**: Internal team discussion
- **Recording**: No (confidential team feedback)
- **Attendees**: Development team only

#### Ad-hoc Technical Discussions

- **Schedule**: As needed
- **Format**: Quick calls, WhattsApp or scheduled meetings
- **Purpose**: Architectural decisions, problem-solving, code walkthroughs

---

## Office 365 / Outlook

### Email Communication

**Primary Use Cases**:

- External stakeholder communication
- Formal approvals (PRD sign-offs)
- Contract and license management
- Communication with YHT corporate teams

**Internal Communication**: Prefer Teams for faster response

### Calendar Management

**Meeting Scheduling**:

- All recurring ceremonies (standups, sprint planning) in Outlook calendar
- Outlook calendar synced with Teams for easy meeting join
- Meeting invites sent via Outlook

### Document Collaboration

**SharePoint/OneDrive** (part of Office 365):

- Initial drafts of PRDs and formal documents
- Long-term archive of approved PRDs

**Workflow**:

1. Draft document in Word (using corporate template)
2. Share via OneDrive / Email for review
3. Finalize and get approval
4. Archive in SharePoint
5. Technical specs move to GitHub repos

---

## Collaboration Best Practices

### Asynchronous Communication

- Document decisions in GitHub issues/PRs
- Use Teams / WhattsApp for announcements (not just chat)
- Write clear commit messages for future reference

### Synchronous Communication

- Daily standup for quick coordination
- Impromptu Teams calls for complex discussions
- Screen sharing for code walkthroughs

### Tool Selection Guide

| Scenario            | Tool                            |
| ------------------- | ------------------------------- |
| Task tracking       | GitHub Issues                   |
| Code discussion     | GitHub PR comments              |
| Quick question      | Teams chat                      |
| Live demo           | Teams meeting with screen share |
| Formal approval     | Outlook email                   |
| Document draft      | OneDrive/SharePoint             |
| Final documentation | GitHub repository               |

---

_Last Updated: November 2025_  
_Version: 1.0_
