# Platform Architecture Overview

## Executive Summary

The Kinana Platform is a cloud-native educational Learning Resource Management System (LRMS) built on a microservices architecture and deployed on Azure Kubernetes Service (AKS). The platform provides comprehensive learning tools, content management, and LTI (Learning Tools Interoperability) integration capabilities across multiple domains and subdomains.

## Key Characteristics

### Architecture Style
**Microservices Architecture**
- Promotes modularity and scalability
- Enables independent service deployment
- Facilitates team autonomy and faster development cycles

### Cloud Provider
**Microsoft Azure**
- Provides robust infrastructure for cloud-based services
- Ensures high availability and disaster recovery
- Offers integrated security and compliance features

### Orchestration
**Azure Kubernetes Service (AKS)**
- Manages and scales containerized applications
- Provides automated deployment and rollback capabilities
- Ensures efficient resource utilization

### Domain
**kinana.ai**
- Represents the digital identity and brand
- Provides consistent naming across all services

### Deployment Model
**Multi-tenant, Containerized Services**
- Supports multiple organizations on shared infrastructure
- Ensures data isolation and security
- Optimizes resource utilization and cost efficiency

## High-Level Architecture

The Kinana Platform follows a distributed microservices architecture pattern organized into six distinct layers:

### Layer 1: Internet / Users
- All external traffic enters through public DNS endpoints
- Supports global accessibility
- Routes users to appropriate services

### Layer 2: Ingress & TLS Termination
- **NGINX Ingress Controller** handles all incoming requests
- Manages 18+ SSL certificates using cert-manager
- Utilizes Let's Encrypt for automated certificate provisioning
- Provides TLS termination for secure communications

### Layer 3: Core Services
Three primary services handle authentication, API routing, and administration:
- **Identity Services**: Authentication and Authorization
- **API Gateway**: Request routing and aggregation
- **Admin Interface**: System management and configuration

### Layer 4: Application Services
Specialized microservices for specific functionality:
- PDF processing services (optimization, translation, image extraction)
- Document management services
- Translation services
- LTI integration services
- Web applications

### Layer 5: Data Layer
Three primary data stores:
- **Redis Cache**: Session storage and application state
- **MySQL**: File system metadata
- **SQL Server**: LTI integration data (external host)

### Layer 6: Storage Layer
- **Azure Blob Storage** with CSI Driver
- Provides 10 persistent volumes totaling 100Gi
- Stores files, documents, and media

## Technology Stack

### Orchestration
- **Azure Kubernetes Service (AKS)**: Production cluster management

### Service Mesh
- **NGINX Ingress Controller**: Latest stable version

### Certificate Management
- **cert-manager**: Automated Let's Encrypt certificate provisioning

### Storage
- **Azure Blob Storage CSI Driver**: Persistent volume management (blob.csi.azure.com)

### Caching
- **Redis 6.0.8** (Bitnami): High-performance in-memory data store

### Databases
- **MySQL**: File system metadata storage
- **SQL Server** (External: 10.7.0.4): LTI integration data

### Container Registry
- **Azure Container Registry**: uepcr.azurecr.io

### Secret Management
- **Azure Key Vault**: ibt-prd-kv-01

### Runtime
- **.NET Core**: ASP.NET Core services
- **Node.js**: Express.js applications

## Domain Structure

### Primary Domain
**kinana.ai** - Main platform domain

### Subdomain Organization

#### Identity Services
- `id.kinana.ai` - Identity & Authentication
- `*.id.kinana.ai` - Multi-tenant Identity (wildcard)

#### Administration
- `admin.kinana.ai` - Administration Panel
- `*.admin.kinana.ai` - Multi-tenant Admin (wildcard)

#### Applications
- `app.kinana.ai` - Main Application
- `*.app.kinana.ai` - Multi-tenant Apps (wildcard)

#### API Services
- `api.kinana.ai` - API Gateway

#### Library Services
- `lib.kinana.ai` - Library/Resources
- `*.lib.kinana.ai` - Multi-tenant Library (wildcard)

#### Experiments
- `lab.kinana.ai` - Experiments (Brokkly)
- `*.lab.kinana.ai` - Multi-tenant Experiments (wildcard)

#### Media Services
- `vid.kinana.ai` - Video Services
- `*.vid.kinana.ai` - Multi-tenant Video (wildcard)
- `snd.kinana.ai` - Audio/Sound Services
- `*.snd.kinana.ai` - Multi-tenant Sound (wildcard)

#### LTI Integration
- `lti.kinana.ai` - LTI Integration
- `*.lti.kinana.ai` - Multi-tenant LTI (wildcard)

#### Special Services
- `pdfopt.kinana.ai` - PDF Optimization
- `pdftra.kinana.ai` - PDF Translation
- `kintra.kinana.ai` - Language Translation
- `pdfimg.kinana.ai` - PDF Image Extraction

#### Public Website
- `www.kinana.ai` - Marketing Website

#### Legacy Domains
- `akadimi.io` - Legacy platform (docs, fsapi, pdf services)

## Design Principles

### 1. Microservices Independence
Each service is independently deployable, scalable, and maintainable.

### 2. Cloud-Native Design
Built specifically for cloud environments with containerization at its core.

### 3. Multi-Tenancy
Supports multiple organizations with data isolation and security.

### 4. Security First
TLS encryption for all external traffic, automated certificate management, and comprehensive secret management.

### 5. Scalability
Horizontal scaling capabilities through Kubernetes orchestration.

### 6. Resilience
Automated health checks, self-healing capabilities, and redundancy.

## Service Communication Patterns

### Internal Communication
- Services communicate via Kubernetes internal DNS
- Service naming convention: `<service-name>.kinana-dev.svc.cluster.local`
- No authentication required for internal calls
- Redis cache shared across services

### External Communication
- All external traffic routed through NGINX Ingress
- TLS termination at ingress level
- Header preservation with underscores_in_headers enabled

### Database Connections
- **MySQL**: Internal cluster service (fsdb)
- **SQL Server**: External host (10.7.0.4:1433)
- Encrypted connections with trust server certificate

## Deployment Strategy

### Container Registry
- **Azure Container Registry (ACR)**: uepcr.azurecr.io
- Docker registry authentication
- Pull Policy: Always (ensures latest images)

### Image Naming Convention
`<service-name>:<version>_<environment>`

**Examples:**
- Development: `1.0.0_dev`, `1.3.0_dev`
- Production: `1.0.0`

### Namespace Strategy
- **kinana-dev**: All current application services and production workloads
- **akadimi-stg**: Legacy storage volumes and migration artifacts

### Resource Management
- Default replicas: 1
- Image pull policy: Always
- Node selector: Linux
- Horizontal Pod Autoscaling (HPA) ready
- Cluster autoscaling via AKS

## Key Features

### 1. LTI Integration
- LTI 1.3 (Learning Tools Interoperability)
- OAuth 2.0 + OpenID Connect
- Integration with external LMS platforms
- Grade passback capabilities

### 2. PDF Processing
- Optimization for reduced file sizes
- Translation capabilities
- Image extraction
- Viewing and rendering

### 3. Multi-Language Support
- Content translation services
- PDF translation
- Language-specific interfaces

### 4. Document Management
- Comprehensive file system
- Metadata storage
- Version control
- Access management

### 5. Multi-Tenant Architecture
- Wildcard subdomain support
- Data isolation per tenant
- Shared infrastructure
- Independent customization

## Performance Considerations

### Caching Strategy
- Redis for session storage
- Application state management
- Query result caching
- 30-day caching for static assets (/api/files/*)

### Load Balancing
- NGINX ingress controller
- Round-robin distribution
- Session affinity support
- Health check integration

### File Upload Support
- Maximum body size: 1500M (configurable to 2GB)
- Chunked upload support
- Progress tracking
- Resume capability

## Monitoring and Observability

### Recommended Tools
- Azure Monitor for AKS
- Prometheus + Grafana
- Application Insights
- NGINX Ingress metrics

### Key Metrics
- Pod CPU/Memory usage
- Request latency
- Error rates
- Certificate expiration dates
- Storage utilization

### Logging Strategy
- Application logs: Container stdout/stderr
- Ingress logs: Access and error logs
- System logs: Kubernetes events
- Audit logs: API server audit logs

## Future Considerations

### Scalability Enhancements
- Multi-region deployment for global reach
- CDN integration for static assets
- Database read replicas for query scaling
- Message queue (RabbitMQ/Kafka) for async processing
- Service mesh for advanced traffic management

### Observability Improvements
- Distributed tracing (Jaeger/Zipkin)
- Centralized logging (ELK/EFK stack)
- Advanced monitoring (Prometheus + Thanos)
- SLO/SLA tracking with error budgets

### Cost Optimization
- Spot instances for non-critical workloads
- Storage lifecycle policies for blob storage
- Resource right-sizing based on metrics
- Reserved instances for predictable workloads

## Conclusion

The Kinana Platform represents a modern, cloud-native approach to educational content management and delivery. Its microservices architecture provides flexibility, scalability, and resilience while maintaining security and performance. The platform's design supports current needs while providing a foundation for future growth and enhancement.

---

**Document Version**: 1.0  
**Last Updated**: November 2024  
**Classification**: Unclassified
