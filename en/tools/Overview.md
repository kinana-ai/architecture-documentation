# Tools & Resources - Overview

## Purpose

This section documents the development tools, collaboration platforms, templates, and external resources used by the Kinana development team. It provides reference for team members and demonstrates tooling standards for IP governance compliance.

---

## Tool Categories

### Development Tools

Core IDE, plugins, and local development environment setup for Kinana platform development.

- **Primary IDE**: Visual Studio Code (Windows 10/11)
- **Local Environment**: Docker Desktop, GitHub integration
- **Specialized Hardware**: Ubuntu workstation with GPU for AI development
- **Mobile Development**: macOS environments for future iOS development

### Collaboration Tools

Platforms enabling team coordination, communication, and infrastructure access.

- **Communication**: Microsoft Teams (YHT corporate), Office 365, Outlook
- **Project Management**: GitHub Projects (Kanban board)
- **Infrastructure Access**: Microsoft Azure portal and CLI tools

### Templates & Checklists

Standardized templates for documentation and code, plus reference checklists for quality processes.

- **Document Templates**: YHT/Ibtikar corporate templates (Word, Markdown)
- **Code Templates**: Standard VS Code scaffolding for Angular/ABP.io
- **Review Checklists**: Code review and testing checklists

### External Resources

Third-party platforms, frameworks, and documentation for licensed tools.

- **ABP.io Framework**: Commercial license with Studio tool access
- **PSPDF/Nutrient**: PDF processing and viewing (yearly license)
- **GDPicture**: Image and document processing library
- **Training Materials**: Framework documentation and best practices

---

## Platform Context

### Development Machine Configuration

**Primary Workstations**: Windows 10/11 desktops

- Visual Studio Code with extensions
- Docker Desktop
- GitHub Desktop or Git CLI
- Local folder structure mirroring repository structure
- Node.js, Angular CLI, .NET SDK

**Infrastructure Access Workstations**: Windows + macOS

- Solution Architect and Senior Developer: Azure CLI and portal access
- Azure Kubernetes tools (kubectl, Helm)
- SSH access to staging infrastructure

**Specialized Workstation**: Ubuntu desktop

- NVIDIA 4090 GPU
- CUDA toolkit and AI/ML libraries
- Local AI model development and testing

**Future Mobile Development**: macOS machines

- Xcode (iOS development)
- Android Studio (optional)
- Mobile emulators and testing tools

### Development Workflow Integration

```
Local VS Code → Docker Local Build → GitHub Repo → Azure Staging → QA Testing
       ↓              ↓                    ↓            ↓
   Live Reload    Container Test    Code Review   Integration Test
```

---

## Licensed Tools & Frameworks

### ABP.io Commercial License

- **License Type**: Multi-developer commercial license
- **Usage**: Backend framework, Admin UI, ABP Studio access
- **Components**:
  - ABP Framework modules
  - Admin interface templates
  - ABP Studio for code generation and management
- **Documentation**: [ABP.io Documentation](https://docs.abp.io)

### PSPDF/Nutrient PDF Platform

- **License Type**: Yearly contract
- **Usage**: PDF viewing, rendering, annotation in Library sub-app
- **Components**: PDF viewer SDK, backend processing
- **Documentation**: [Nutrient Documentation](https://www.nutrient.io/guides/)

### GDPicture Library

- **License Type**: Included in PSPDF contract
- **Usage**:
  - Text extraction from PDFs
  - Image extraction and optimization
  - Document format conversion
- **Backend Integration**: Admin processing workflows

---

## Communication & Collaboration Standards

### Microsoft Teams (YHT Corporate)

- **Daily standups**: Video meetings
- **Sprint planning & reviews**: Team sessions
- **Ad-hoc discussions**: Chat and quick calls
- **Screen sharing**: Code walkthroughs and demos

### Office 365 / Outlook

- **Email**: External stakeholder communication
- **Calendar**: Meeting scheduling
- **Document sharing**: Initial document collaboration (prior to GitHub commit)

### GitHub Projects

- **Project Management**: Kanban board for task tracking
- **Issue Tracking**: All development tasks and bugs
- **Sprint Management**: Milestones and labels for sprint organization
- **Code Review**: Pull request workflows

**Note**: Team does not use Jira. All project management occurs in GitHub Projects.

---

## Document Management

### Product Requirements Documents (PRDs)

- **Author**: Product Manager
- **Format**: Word documents using YHT/Ibtikar templates
- **Approval**: Signed off by stakeholders and management
- **Purpose**: Formal authorization to proceed with development

### Technical Documentation

- **Format**: Markdown (.md) files in repositories
- **Location**: Repository-specific README files and `/docs` folders
- **Maintenance**: Developers update as part of feature development

### Templates

All team members have access to:

- Yas Holding Technology document templates (Word)
- Ibtikar Edu Tech Solutions document templates (Word)
- Standard markdown templates for technical documentation

---

## Code Standards

### Source Code Headers

All source files include copyright header:

```typescript
/**
 * Copyright (c) 2024 Yas Holding Technology - YHT EdTech Division
 * Kinana Content Hub Platform
 *
 * This code is proprietary and confidential.
 */
```

### File Creation

- **Frontend (Angular)**: Standard VS Code Angular component/service/module creation
- **Backend (ABP.io)**: ABP CLI or ABP Studio for entity, service, and controller generation
- **Configuration**: Manual creation following established patterns

### Coding Conventions

- Follow ABP.io best practices for backend
- Angular style guide for frontend
- Prettier formatting enforced via VS Code extension
- ESLint/TSLint for code quality

---

## Tool Access & Onboarding

### New Developer Setup

1. Provision Windows 10/11 workstation
2. Install VS Code with required extensions
3. Install Docker Desktop
4. Configure GitHub access (SSH keys)
5. Install Node.js, Angular CLI, .NET SDK
6. Clone relevant repositories
7. Run local environment setup scripts

### Infrastructure Access (Senior Roles)

- Azure portal credentials provided by Solution Architect
- kubectl configuration for staging cluster
- SSH keys for server access (if needed)

### Licensed Tool Access

- ABP Studio credentials managed by Solution Architect
- PSPDF/Nutrient license keys in environment configuration
- GDPicture integration configured in backend services

---

## Tool Maintenance

### Updates & Upgrades

- VS Code extensions: Auto-update enabled
- Docker Desktop: Quarterly update cycle
- Framework versions: Managed via package managers (npm, NuGet)
- Licensed tools: Reviewed during annual renewal

### License Management

- Solution Architect maintains license inventory
- Annual renewals coordinated by Product Manager
- License keys stored securely (not in source code)

---

_Last Updated: November 2025_  
_Version: 1.0_
