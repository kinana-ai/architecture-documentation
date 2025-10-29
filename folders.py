#!/usr/bin/env python3
"""
KINANA Wiki Folder Structure Creator
Creates complete folder structure for KINANA platform documentation with README files.
Prepares structure for GitHub check-in.

Usage:
    python create_kinana_folders.py
    
Author: YHT EdTech Development Team
Date: 2025
"""

import os
import sys
from pathlib import Path
from datetime import datetime

# ANSI color codes for console output (works on Windows 10+ with ANSI support)
class Colors:
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'

def print_header():
    """Print script header"""
    print(f"\n{Colors.BOLD}{Colors.BLUE}{'='*70}")
    print("KINANA Platform Wiki - Folder Structure Creator")
    print(f"{'='*70}{Colors.END}\n")

def print_success(message):
    """Print success message"""
    print(f"{Colors.GREEN}✓ {message}{Colors.END}")

def print_info(message):
    """Print info message"""
    print(f"{Colors.BLUE}ℹ {message}{Colors.END}")

def print_warning(message):
    """Print warning message"""
    print(f"{Colors.YELLOW}⚠ {message}{Colors.END}")

def print_error(message):
    """Print error message"""
    print(f"{Colors.RED}✗ {message}{Colors.END}")

# Complete folder structure for KINANA Wiki
FOLDER_STRUCTURE = [
    # 1. Home / Overview
    "home",
    
    # 2. Platform Architecture
    "architecture",
    "architecture/data-architecture",
    "architecture/security",
    
    # 3. Technical Documentation
    "technical",
    "technical/api",
    "technical/frontend",
    "technical/backend",
    "technical/database",
    "technical/devops",
    
    # 4. Source Documentation Standards
    "standards",
    "standards/code-documentation",
    "standards/file-headers",
    "standards/adr",
    
    # 5. Intellectual Property Documentation
    "ip",
    "ip/copyright",
    "ip/patents",
    "ip/trade-secrets",
    "ip/trademarks",
    "ip/third-party-licenses",
    "ip/procedures",
    "ip/contributions",
    
    # 6. Development Standards
    "development-standards",
    "development-standards/coding",
    "development-standards/git",
    "development-standards/testing",
    "development-standards/security",
    "development-standards/qa",
    
    # 7. Operations & Deployment
    "operations",
    "operations/deployment",
    "operations/monitoring",
    "operations/incident-management",
    "operations/maintenance",
    "operations/disaster-recovery",
    
    # 8. User Documentation
    "user-guide",
    "user-guide/admin",
    "user-guide/integration",
    
    # 9. Compliance & Governance
    "compliance",
    "compliance/regulatory",
    "compliance/privacy",
    "compliance/accessibility",
    "compliance/localization",
    "compliance/security",
    
    # 10. Processes & Workflows
    "processes",
    "processes/development",
    "processes/code-review",
    "processes/change-management",
    "processes/release-management",
    
    # 11. Tools & Resources
    "tools",
    "tools/development",
    "tools/collaboration",
    "tools/templates",
    "tools/resources",
    
    # 12. Team & Contacts
    "team",
    "team/onboarding",
    
    # 13. Knowledge Base
    "knowledge-base",
    "knowledge-base/troubleshooting",
    "knowledge-base/best-practices",
    "knowledge-base/lessons-learned",
    
    # 14. Reference
    "reference",
    "reference/version-history",
    "reference/dependencies",
    "reference/metrics",
]

# Section descriptions for README generation
SECTION_DESCRIPTIONS = {
    "home": "Welcome to KINANA Platform Documentation",
    "architecture": "Platform Architecture Documentation",
    "architecture/data-architecture": "Data Architecture and Database Design",
    "architecture/security": "Security Architecture and Standards",
    "technical": "Technical Documentation Hub",
    "technical/api": "API Reference Documentation",
    "technical/frontend": "Frontend Architecture and Components",
    "technical/backend": "Backend Services and Business Logic",
    "technical/database": "Database Schema and Documentation",
    "technical/devops": "DevOps and Infrastructure Documentation",
    "standards": "Documentation Standards and Guidelines",
    "standards/code-documentation": "Code Documentation Standards",
    "standards/file-headers": "File Header Standards and Templates",
    "standards/adr": "Architecture Decision Records",
    "ip": "Intellectual Property Documentation",
    "ip/copyright": "Copyright Documentation and Registration",
    "ip/patents": "Patent Portfolio and Applications",
    "ip/trade-secrets": "Trade Secret Registry and Protection",
    "ip/trademarks": "KINANA Trademark and Brand Guidelines",
    "ip/third-party-licenses": "Third-Party License Inventory",
    "ip/procedures": "IP Management Procedures",
    "ip/contributions": "Contribution Guidelines and IP Assignment",
    "development-standards": "Development Standards and Best Practices",
    "development-standards/coding": "Coding Standards and Style Guides",
    "development-standards/git": "Git Workflow and Version Control",
    "development-standards/testing": "Testing Standards and Requirements",
    "development-standards/security": "Security Standards and Practices",
    "development-standards/qa": "Quality Assurance Standards",
    "operations": "Operations and Deployment Documentation",
    "operations/deployment": "Deployment Procedures and Guides",
    "operations/monitoring": "Monitoring and Observability",
    "operations/incident-management": "Incident Response and Management",
    "operations/maintenance": "Maintenance Procedures and Schedules",
    "operations/disaster-recovery": "Disaster Recovery and Business Continuity",
    "user-guide": "User Documentation and Guides",
    "user-guide/admin": "Administrator Guide and Documentation",
    "user-guide/integration": "Integration Guides and Tutorials",
    "compliance": "Compliance and Governance Documentation",
    "compliance/regulatory": "Regulatory Compliance (PDPL, GDPR, etc.)",
    "compliance/privacy": "Data Privacy Policies and Procedures",
    "compliance/accessibility": "Accessibility Standards (WCAG 2.1 AA)",
    "compliance/localization": "Localization and Arabic Support",
    "compliance/security": "Security Compliance and Audits",
    "processes": "Development Processes and Workflows",
    "processes/development": "Development Workflow and Sprint Process",
    "processes/code-review": "Code Review Process and Guidelines",
    "processes/change-management": "Change Management Procedures",
    "processes/release-management": "Release Management and Planning",
    "tools": "Tools and Resources Documentation",
    "tools/development": "Development Tools and Setup",
    "tools/collaboration": "Collaboration Tools and Guidelines",
    "tools/templates": "Templates and Checklists",
    "tools/resources": "External Resources and Links",
    "team": "Team Structure and Contacts",
    "team/onboarding": "New Team Member Onboarding",
    "knowledge-base": "Knowledge Base and Troubleshooting",
    "knowledge-base/troubleshooting": "Troubleshooting Guides and Solutions",
    "knowledge-base/best-practices": "Best Practices and Design Patterns",
    "knowledge-base/lessons-learned": "Lessons Learned and Post-Mortems",
    "reference": "Reference Documentation",
    "reference/version-history": "Version History and Changelog",
    "reference/dependencies": "Dependencies and Technology Stack",
    "reference/metrics": "Metrics and KPIs Dashboard",
}

def get_readme_content(folder_path):
    """Generate README.md content for a folder"""
    folder_name = os.path.basename(folder_path)
    description = SECTION_DESCRIPTIONS.get(folder_path, "Documentation Section")
    
    # Create title from folder name
    title = folder_name.replace('-', ' ').title()
    
    content = f"""# {title}

## Overview

{description}

---

## Contents

This section contains documentation for {folder_name}.

### Documentation Structure

*Add links to specific documentation files here.*

---

## Quick Links

- [KINANA Home](../README.md)
- [Platform Overview](../home/README.md)
- [Technical Documentation](../technical/README.md)

---

## Contributing

See [Contributing Guidelines](../CONTRIBUTING.md) for information on how to contribute to this documentation.

---

## License

Documentation is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
Code examples are licensed under the [MIT License](../LICENSE-CODE.md).

© {datetime.now().year} YHT LLC. KINANA is a trademark of YHT LLC.

---

*Last Updated: {datetime.now().strftime('%Y-%m-%d')}*
"""
    return content

def create_folder_structure(base_path="."):
    """Create the complete folder structure with README files"""
    base_path = Path(base_path)
    created_folders = []
    created_files = []
    skipped_folders = []
    
    print_info(f"Creating folder structure in: {base_path.absolute()}")
    print_info(f"Total folders to create: {len(FOLDER_STRUCTURE)}")
    print()
    
    for folder in FOLDER_STRUCTURE:
        folder_path = base_path / folder
        readme_path = folder_path / "README.md"
        
        try:
            # Create folder if it doesn't exist
            if not folder_path.exists():
                folder_path.mkdir(parents=True, exist_ok=True)
                created_folders.append(str(folder))
                print_success(f"Created folder: {folder}/")
            else:
                skipped_folders.append(str(folder))
                print_info(f"Folder exists: {folder}/")
            
            # Create README.md if it doesn't exist
            if not readme_path.exists():
                readme_content = get_readme_content(folder)
                readme_path.write_text(readme_content, encoding='utf-8')
                created_files.append(str(folder) + "/README.md")
                print_success(f"Created README: {folder}/README.md")
            else:
                print_info(f"README exists: {folder}/README.md")
                
        except Exception as e:
            print_error(f"Error creating {folder}: {str(e)}")
    
    return created_folders, created_files, skipped_folders

def create_root_readme(base_path="."):
    """Create root README.md for the repository"""
    base_path = Path(base_path)
    readme_path = base_path / "README.md"
    
    if readme_path.exists():
        print_info("Root README.md already exists, skipping...")
        return False
    
    content = f"""# KINANA Platform Documentation

> Comprehensive documentation for the KINANA educational technology platform

[![License: CC BY 4.0](https://img.shields.io/badge/Docs-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Code: MIT](https://img.shields.io/badge/Code-MIT-yellow.svg)](LICENSE-CODE.md)

---

## 📋 About KINANA

KINANA is an advanced educational technology platform developed by YHT EdTech Division, serving the UAE, GCC, and Egypt markets. This repository contains comprehensive documentation covering architecture, development standards, API references, and operational procedures.

---

## 🗂️ Documentation Structure

### 1. [Home & Overview](home/)
Welcome to KINANA, getting started guides, and quick start tutorials.

### 2. [Platform Architecture](architecture/)
System architecture, data models, security design, and infrastructure documentation.

### 3. [Technical Documentation](technical/)
API references, frontend/backend architecture, database schemas, and DevOps guides.

### 4. [Source Documentation Standards](standards/)
Code documentation standards, file headers, README templates, and ADRs.

### 5. [Intellectual Property Documentation](ip/)
Copyright, patents, trade secrets, trademarks, and license management.

### 6. [Development Standards](development-standards/)
Coding standards, version control workflows, testing requirements, and security practices.

### 7. [Operations & Deployment](operations/)
Deployment procedures, monitoring, incident management, and disaster recovery.

### 8. [User Documentation](user-guide/)
End-user guides, administrator documentation, and integration tutorials.

### 9. [Compliance & Governance](compliance/)
Regulatory compliance (PDPL, GDPR), accessibility (WCAG 2.1 AA), and localization.

### 10. [Processes & Workflows](processes/)
Development workflows, code review processes, and release management.

### 11. [Tools & Resources](tools/)
Development tools, collaboration platforms, templates, and external resources.

### 12. [Team & Contacts](team/)
Team structure, roles, contact information, and onboarding guides.

### 13. [Knowledge Base](knowledge-base/)
Troubleshooting guides, best practices, lessons learned, and case studies.

### 14. [Reference](reference/)
Glossary, version history, dependencies, and platform metrics.

---

## 🚀 Quick Start

1. **New to KINANA?** Start with the [Getting Started Guide](home/getting-started.md)
2. **Looking for APIs?** See [API Documentation](technical/api/)
3. **Need to deploy?** Check [Deployment Guide](operations/deployment/)
4. **Contributing?** Read [Contributing Guidelines](CONTRIBUTING.md)

---

## 📝 Contributing

We welcome contributions to KINANA documentation! Please read our [Contributing Guidelines](CONTRIBUTING.md) before submitting changes.

### Quick Contribution Steps

1. Fork this repository
2. Create a feature branch (`git checkout -b feature/improve-docs`)
3. Make your changes following our [Documentation Standards](standards/)
4. Submit a pull request

---

## 📄 License

### Documentation
All documentation is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

You are free to share and adapt the documentation with appropriate attribution to YHT LLC.

### Code Examples
Code examples and snippets in this documentation are licensed under the [MIT License](LICENSE-CODE.md).

---

## 🔒 Confidential Content

Some sections of this documentation contain confidential information:
- [IP Documentation](ip/) - Restricted access
- [Security Documentation](compliance/security/) - Restricted access

Access to confidential sections requires appropriate authorization.

---

## 📧 Contact

- **General Inquiries:** info@yht.com
- **Technical Support:** support@kinana.com
- **Legal/IP Questions:** legal@yht.com

---

## 🏢 About YHT LLC

YHT LLC is a leading educational technology provider serving the Middle East and North Africa region with innovative learning solutions.

**KINANA®** is a registered trademark of YHT LLC.

---

© {datetime.now().year} YHT LLC. All rights reserved.

*Last Updated: {datetime.now().strftime('%Y-%m-%d')}*
"""
    
    try:
        readme_path.write_text(content, encoding='utf-8')
        print_success("Created root README.md")
        return True
    except Exception as e:
        print_error(f"Error creating root README.md: {str(e)}")
        return False

def create_gitignore(base_path="."):
    """Create .gitignore file"""
    base_path = Path(base_path)
    gitignore_path = base_path / ".gitignore"
    
    if gitignore_path.exists():
        print_info(".gitignore already exists, skipping...")
        return False
    
    content = """# KINANA Documentation .gitignore

# OS Files
.DS_Store
Thumbs.db
desktop.ini

# Editor files
.vscode/
.idea/
*.swp
*.swo
*~
.project
.settings/

# Backup files
*.bak
*.tmp
*.temp

# Logs
*.log

# Build artifacts
_build/
.cache/

# Python
__pycache__/
*.py[cod]
*$py.class
.Python
venv/
env/

# Node
node_modules/
npm-debug.log*

# Confidential files (if accidentally added)
*.secret
*.private
**/secrets/

# Local configuration
.env
.env.local
"""
    
    try:
        gitignore_path.write_text(content, encoding='utf-8')
        print_success("Created .gitignore")
        return True
    except Exception as e:
        print_error(f"Error creating .gitignore: {str(e)}")
        return False

def create_contributing_guide(base_path="."):
    """Create CONTRIBUTING.md file"""
    base_path = Path(base_path)
    contributing_path = base_path / "CONTRIBUTING.md"
    
    if contributing_path.exists():
        print_info("CONTRIBUTING.md already exists, skipping...")
        return False
    
    content = f"""# Contributing to KINANA Documentation

Thank you for your interest in contributing to KINANA platform documentation!

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How to Contribute](#how-to-contribute)
- [Documentation Standards](#documentation-standards)
- [Pull Request Process](#pull-request-process)

---

## Code of Conduct

We are committed to providing a welcoming and inspiring community for all. Please be respectful and professional in all interactions.

---

## How to Contribute

### Reporting Issues

If you find errors, outdated information, or missing documentation:

1. Check if an issue already exists
2. Create a new issue with:
   - Clear description of the problem
   - Location of the issue (file/section)
   - Suggested improvement (if applicable)

### Suggesting Enhancements

Have ideas for improving the documentation? We'd love to hear them!

1. Open an issue describing your suggestion
2. Explain why it would be valuable
3. Provide examples if possible

### Submitting Changes

1. **Fork the repository**
2. **Create a branch** (`git checkout -b feature/improve-api-docs`)
3. **Make your changes** following our standards
4. **Test your changes** (verify links, formatting, etc.)
5. **Commit your changes** with clear commit messages
6. **Push to your fork** (`git push origin feature/improve-api-docs`)
7. **Open a Pull Request**

---

## Documentation Standards

### File Naming
- Use lowercase with hyphens: `api-authentication.md`
- Be descriptive: `database-migration-guide.md`

### Markdown Style
- Use proper heading hierarchy (H1 → H2 → H3)
- Add blank lines around headings
- Use code blocks with language specification
- Include alt text for images

### Content Guidelines
- Write clearly and concisely
- Use active voice
- Include examples where helpful
- Keep documentation up-to-date
- Add dates to time-sensitive content

### Links
- Use relative links for internal docs
- Test all links before submitting
- Use descriptive link text

---

## Pull Request Process

1. **Update README** if you add new sections
2. **Follow standards** outlined in [Documentation Standards](standards/)
3. **Write clear descriptions** of your changes
4. **Reference issues** if applicable (#123)
5. **Wait for review** from maintainers
6. **Address feedback** promptly

### PR Checklist

- [ ] Documentation follows style guide
- [ ] All links are tested and working
- [ ] Spelling and grammar checked
- [ ] No confidential information included
- [ ] Copyright headers added where needed
- [ ] Changes tested locally

---

## License

By contributing, you agree that your contributions will be licensed under the same license as this project:
- Documentation: CC BY 4.0
- Code examples: MIT License

---

## Questions?

Contact the documentation team:
- Email: docs@kinana.com
- Teams: #kinana-docs channel

---

Thank you for contributing to KINANA! 🎉

© {datetime.now().year} YHT LLC
"""
    
    try:
        contributing_path.write_text(content, encoding='utf-8')
        print_success("Created CONTRIBUTING.md")
        return True
    except Exception as e:
        print_error(f"Error creating CONTRIBUTING.md: {str(e)}")
        return False

def print_summary(created_folders, created_files, skipped_folders):
    """Print summary of operations"""
    print(f"\n{Colors.BOLD}{Colors.BLUE}{'='*70}")
    print("Summary")
    print(f"{'='*70}{Colors.END}\n")
    
    print(f"{Colors.GREEN}✓ Folders created: {len(created_folders)}{Colors.END}")
    print(f"{Colors.GREEN}✓ Files created: {len(created_files)}{Colors.END}")
    
    if skipped_folders:
        print(f"{Colors.YELLOW}⚠ Folders already existed: {len(skipped_folders)}{Colors.END}")
    
    print(f"\n{Colors.BOLD}Total structure: {len(FOLDER_STRUCTURE)} folders{Colors.END}\n")

def print_next_steps():
    """Print next steps for the user"""
    print(f"{Colors.BOLD}{Colors.BLUE}{'='*70}")
    print("Next Steps")
    print(f"{'='*70}{Colors.END}\n")
    
    print(f"{Colors.BOLD}1. Review the generated structure:{Colors.END}")
    print(f"   {Colors.BLUE}explorer .{Colors.END}  (Windows)")
    print(f"   {Colors.BLUE}open .{Colors.END}      (Mac)")
    print(f"   {Colors.BLUE}ls -la{Colors.END}      (Linux)\n")
    
    print(f"{Colors.BOLD}2. Initialize Git (if not already initialized):{Colors.END}")
    print(f"   {Colors.BLUE}git init{Colors.END}")
    print(f"   {Colors.BLUE}git add .{Colors.END}")
    print(f"   {Colors.BLUE}git commit -m \"feat: Initialize KINANA Wiki documentation structure\"{Colors.END}\n")
    
    print(f"{Colors.BOLD}3. Push to GitHub:{Colors.END}")
    print(f"   {Colors.BLUE}git remote add origin <your-repo-url>{Colors.END}")
    print(f"   {Colors.BLUE}git branch -M main{Colors.END}")
    print(f"   {Colors.BLUE}git push -u origin main{Colors.END}\n")
    
    print(f"{Colors.BOLD}4. Start adding content:{Colors.END}")
    print(f"   - Edit README.md files in each folder")
    print(f"   - Add markdown documentation files")
    print(f"   - Follow the structure defined in Wiki TOC\n")

def main():
    """Main execution function"""
    print_header()
    
    # Ask user for target directory
    print(f"{Colors.BOLD}Where do you want to create the folder structure?{Colors.END}")
    print(f"Press Enter for current directory, or specify path:")
    
    target_path = input(f"{Colors.BLUE}Path: {Colors.END}").strip()
    
    if not target_path:
        target_path = "."
    
    # Create target directory if it doesn't exist
    target_path_obj = Path(target_path)
    try:
        if not target_path_obj.exists():
            target_path_obj.mkdir(parents=True, exist_ok=True)
            print_success(f"Created target directory: {target_path_obj.absolute()}")
    except Exception as e:
        print_error(f"Could not create target directory: {str(e)}")
        return 1
    
    print()
    
    # Confirm before proceeding
    print(f"{Colors.BOLD}This will create {len(FOLDER_STRUCTURE)} folders with README.md files.{Colors.END}")
    confirm = input(f"{Colors.YELLOW}Continue? (yes/no): {Colors.END}").strip().lower()
    
    if confirm not in ['yes', 'y']:
        print_info("Operation cancelled.")
        return 0
    
    print()
    
    # Create folder structure
    created_folders, created_files, skipped_folders = create_folder_structure(target_path)
    
    print()
    
    # Create root files
    print_info("Creating root documentation files...")
    create_root_readme(target_path)
    create_gitignore(target_path)
    create_contributing_guide(target_path)
    
    # Print summary
    print_summary(created_folders, created_files, skipped_folders)
    
    # Print next steps
    print_next_steps()
    
    print(f"{Colors.GREEN}{Colors.BOLD}✓ KINANA Wiki structure created successfully!{Colors.END}\n")
    
    return 0

if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Operation cancelled by user.{Colors.END}")
        sys.exit(1)
    except Exception as e:
        print_error(f"Unexpected error: {str(e)}")
        sys.exit(1)