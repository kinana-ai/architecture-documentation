# Kinana Platform Architecture Documentation

![Kinana Platform](https://via.placeholder.com/800x200/4A90E2/FFFFFF?text=Kinana+Platform+Architecture)

## Overview

This repository contains comprehensive architecture documentation for the **Kinana Platform** - a cloud-native educational Learning Resource Management System (LRMS) built on microservices architecture and deployed on Azure Kubernetes Service (AKS).

## Table of Contents

### 1. [Platform Architecture Overview](01-Platform-Architecture-Overview.md)
Executive summary of the Kinana Platform, including:
- Key characteristics
- High-level architecture
- Technology stack
- Domain structure
- Design principles

### 2. [System Architecture](02-System-Architecture.md)
Detailed system architecture documentation covering:
- Architecture layers
- Service catalog (20+ microservices)
- Service communication patterns
- Port reference
- Deployment configuration
- Scaling strategies

### 3. [Data Architecture Overview](03-Data-Architecture-Overview.md)
Complete data architecture including:
- Storage strategy (three-tier model)
- Data stores (Redis, MySQL, SQL Server, Azure Blob)
- Data flow patterns
- Caching strategy
- Backup and disaster recovery

### 4. [Database Schema](04-Database-Schema.md)
Detailed database schemas for:
- MySQL (FSDB) - 8 tables with full DDL
- SQL Server (LTI) - 6 tables for LTI integration
- Redis key patterns and data structures
- Schema maintenance procedures

### 5. [Data Architecture](05-Data-Architecture.md) ⭐ **NEW - COMPREHENSIVE**
**33 KB | 1,200+ lines** - Complete data architecture guide:
- Three-tier storage model (detailed)
- All data stores with configurations
- Complete data flow patterns (5 major flows)
- Cache hierarchy and strategies
- Backup and recovery procedures
- Performance optimization
- Cost management
- Monitoring and metrics
- Security considerations
- Future enhancements

### 6. Data Models *(In Development)*
Entity relationship diagrams and data models

### 7. [Security Architecture Overview](07-Security-Architecture-Overview.md)
Comprehensive security documentation:
- Security principles (Defense in Depth, Least Privilege, Zero Trust)
- Security layers (Network, Application, Data, Infrastructure)
- Authentication & authorization
- Secret management
- Audit logging
- Incident response

### 8. [Security Architecture](08-Security-Architecture.md) ⭐ **NEW - COMPREHENSIVE**
**54 KB | 2,100+ lines** - Complete security architecture guide:
- Executive summary with security overview
- Four core security principles (detailed)
- Seven security layers (Network, Application, Data, Infrastructure, etc.)
- Complete authentication & authorization flows
- Encryption strategies (at rest and in transit)
- Access control and data classification
- Secret management (Azure Key Vault + Kubernetes)
- Comprehensive audit logging
- Security monitoring and alerting
- Incident response procedures
- Compliance (GDPR, ISO 27001, SOC 2)
- Future security enhancements

### 9. Authentication & Authorization *(Covered in Security Architecture)*
Detailed auth flows and implementations - See Security Architecture document

### 10. Encryption Standards *(Covered in Security Architecture)*
Encryption at rest and in transit - See Security Architecture document

### 11. Threat Model *(In Development)*
Security threat analysis and mitigation

### 12. [Integration Architecture](11-Integration-Architecture.md)
External system integration including:
- LTI 1.3 integration (complete implementation guide)
- RESTful API documentation
- Webhook integration
- Azure service integration
- Third-party service integration

### 13. [Infrastructure](12-Infrastructure.md)
Infrastructure documentation covering:
- Azure Kubernetes Service (AKS) configuration
- Storage infrastructure
- Container registry
- Networking and DNS
- Monitoring and logging
- CI/CD pipelines
- Cost optimization

## Quick Start

### For Developers

**Understanding the Architecture:**
1. Start with [Platform Architecture Overview](01-Platform-Architecture-Overview.md)
2. Review [System Architecture](02-System-Architecture.md) for service details
3. Check [Integration Architecture](11-Integration-Architecture.md) for API integration

**Working with Data:**
1. Read [Data Architecture Overview](03-Data-Architecture-Overview.md)
2. Review [Database Schema](04-Database-Schema.md) for table structures
3. Understand caching patterns in the data architecture

### For Operations

**Managing Infrastructure:**
1. Review [Infrastructure](12-Infrastructure.md) for cluster configuration
2. Check [Security Architecture](07-Security-Architecture-Overview.md) for security procedures
3. Follow operational procedures in infrastructure docs

### For Integrators

**Integrating with Kinana:**
1. Review [Integration Architecture](11-Integration-Architecture.md)
2. For LMS integration, focus on LTI 1.3 sections
3. For API integration, review API endpoints and authentication

## Key Technologies

### Orchestration & Infrastructure
- **Azure Kubernetes Service (AKS)**: Production cluster orchestration
- **Microsoft Azure**: Cloud provider
- **NGINX Ingress Controller**: Request routing and TLS termination
- **cert-manager**: Automated certificate management

### Application Stack
- **.NET Core**: Microservices framework
- **Node.js**: Web applications and LTI services
- **Redis 6.0.8**: Caching layer
- **MySQL**: File system metadata
- **SQL Server**: LTI integration data

### Storage & Data
- **Azure Blob Storage**: File and document storage (100Gi)
- **Azure Container Registry**: Docker image repository
- **Azure Key Vault**: Secret management

### Security
- **Let's Encrypt**: SSL/TLS certificates
- **OAuth 2.0 / OpenID Connect**: Authentication
- **JWT**: Token-based authorization

## Platform Statistics

### Services
- **Core Services**: 3 (Identity, API Gateway, Admin)
- **Application Services**: 12+ (PDF, Document, Translation, LTI, Web)
- **Data Stores**: 3 (Redis, MySQL, SQL Server)
- **Persistent Volumes**: 10 (100Gi total)

### Domains
- **Primary Domain**: kinana.ai
- **Subdomains**: 18+ including wildcards for multi-tenancy
- **SSL Certificates**: 18+ managed by cert-manager
- **Legacy Domains**: akadimi.io

### Scale
- **Users Served**: ~450,000 annually
- **Markets**: UAE, GCC, Egypt
- **Clients**: Government entities and educational institutions
- **Multi-tenancy**: Supported via wildcard subdomains

## Architecture Highlights

### Microservices Architecture
The platform is built on a distributed microservices architecture with:
- Independent service deployment
- Horizontal scalability
- Service isolation
- Technology flexibility

### Multi-Tenancy
Support for multiple organizations with:
- Wildcard subdomain routing (*.app.kinana.ai, *.admin.kinana.ai)
- Data isolation per tenant
- Independent customization
- Shared infrastructure for cost efficiency

### Cloud-Native Design
Built specifically for cloud environments:
- Containerized services (Docker)
- Kubernetes orchestration
- Automated scaling (HPA, Cluster Autoscaler)
- Infrastructure as Code

### Security-First
Comprehensive security at every layer:
- TLS encryption for all external traffic
- Automated certificate management
- Role-based access control
- Secret management with Azure Key Vault
- Audit logging and monitoring

## Document Versions

| Document | Version | Last Updated |
|----------|---------|--------------|
| All Documents | 1.0 | November 2024 |

## Classification

**Classification Level**: Unclassified

This documentation is intended for internal use and authorized partners. Please handle according to your organization's information security policies.

## Contributing

This documentation is maintained as part of the Kinana Platform development. For updates or corrections:

1. Identify the document that needs updating
2. Make necessary changes
3. Update the version number and last updated date
4. Submit for review

## Document Conventions

### Formatting
- **Bold**: Important terms, technologies, services
- `Code`: Commands, code snippets, configuration values
- _Italic_: Emphasis, file names

### Code Blocks
```yaml
# YAML configuration examples
key: value
```

```javascript
// JavaScript examples
const example = "code";
```

```bash
# Shell commands
kubectl get pods
```

### Tables
Used for structured information, comparisons, and reference data.

### Diagrams
ASCII diagrams for architecture flows and relationships.

## Support

For questions or clarifications about this documentation:
- **Technical Questions**: Contact the development team
- **Infrastructure Questions**: Contact the operations team
- **Integration Questions**: Contact the integration team

## License

© 2024 YHT (Yas Holding Technology) EdTech Division. All rights reserved.

This documentation is proprietary and confidential.

---

## Document Index

### Platform & System
- [01-Platform-Architecture-Overview.md](01-Platform-Architecture-Overview.md) - Executive summary and high-level architecture
- [02-System-Architecture.md](02-System-Architecture.md) - Detailed system architecture and service catalog

### Data Architecture ⭐ **COMPREHENSIVE COVERAGE**
- [03-Data-Architecture-Overview.md](03-Data-Architecture-Overview.md) - Data storage strategy and patterns
- [04-Database-Schema.md](04-Database-Schema.md) - Complete database schemas
- [05-Data-Architecture.md](05-Data-Architecture.md) - **NEW: Complete 33 KB guide covering all data aspects**

### Security ⭐ **COMPREHENSIVE COVERAGE**
- [07-Security-Architecture-Overview.md](07-Security-Architecture-Overview.md) - Security documentation overview
- [08-Security-Architecture.md](08-Security-Architecture.md) - **NEW: Complete 54 KB guide covering all security aspects**

### Integration & Infrastructure
- [11-Integration-Architecture.md](11-Integration-Architecture.md) - External integrations and APIs
- [12-Infrastructure.md](12-Infrastructure.md) - Infrastructure and operations

### Quick Reference
- [QUICK-REFERENCE.md](QUICK-REFERENCE.md) - Essential commands and troubleshooting

---

**Last Updated**: November 19, 2024  
**Documentation Version**: 1.0  
**Platform Version**: Production  
**Total Documentation**: 11 documents, 198 KB, 8,095 lines

### 📊 Visual Diagrams
**NEW**: [DIAGRAMS.md](DIAGRAMS.md) - Complete guide to all 8 SVG architecture diagrams
- Professional scalable vector graphics (SVG format)
- Embedded directly in documentation
- 8 diagrams covering system, data, security, and integration architecture
- Total size: 33 KB | Infinitely scalable

View individual diagrams:
- [layer-architecture.svg](layer-architecture.svg) - 6-layer platform architecture
- [microservices-overview.svg](microservices-overview.svg) - All 20+ microservices
- [service-communication.svg](service-communication.svg) - Service interaction patterns
- [three-tier-storage.svg](three-tier-storage.svg) - Data storage tiers (simple)
- [three-tier-storage-detailed.svg](three-tier-storage-detailed.svg) - Data storage tiers (detailed)
- [defense-in-depth.svg](defense-in-depth.svg) - 7-layer security model
- [zero-trust-flow.svg](zero-trust-flow.svg) - Zero trust security flow
- [lti-architecture.svg](lti-architecture.svg) - LTI 1.3 integration flow
