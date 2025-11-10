# External Resources

## Overview

Kinana development relies on several third-party platforms and frameworks under commercial licenses. This document provides quick reference to documentation and resources for these tools.

---

## ABP.io Framework

### License Information

**License Type**: Multi-developer commercial license  
**License Holder**: Yas Holding Technology - YHT EdTech Division  
**Renewal**: Annual  
**Managed By**: Solution Architect

### What is ABP.io?

ABP (ASP.NET Boilerplate) is a complete architecture and strong infrastructure for creating modern web applications. Kinana uses ABP.io for:

- Backend microservices architecture
- Admin interface and management panels
- Authentication and authorization
- Multi-tenancy support
- Modular application design

### Key Components Used in Kinana

**ABP Framework Modules**:

- Identity Management
- Tenant Management
- Audit Logging
- Settings Management
- Permission System

**Admin Interface**:

- User management
- Role and permission management
- System settings
- Audit log viewing
- Tenant administration

**ABP Studio**:

- Code generation tool
- Solution management
- Database migration tools
- Module scaffolding

### Documentation Links

**Main Documentation**: [https://docs.abp.io](https://docs.abp.io)

**Quick Links**:

- Getting Started: [https://docs.abp.io/en/abp/latest/Getting-Started](https://docs.abp.io/en/abp/latest/Getting-Started)
- Application Development: [https://docs.abp.io/en/abp/latest/Tutorials/Part-1](https://docs.abp.io/en/abp/latest/Tutorials/Part-1)
- Microservices Architecture: [https://docs.abp.io/en/abp/latest/Microservice-Architecture](https://docs.abp.io/en/abp/latest/Microservice-Architecture)
- API Documentation: [https://docs.abp.io/en/abp/latest/API](https://docs.abp.io/en/abp/latest/API)
- Module Development: [https://docs.abp.io/en/abp/latest/Module-Development-Basics](https://docs.abp.io/en/abp/latest/Module-Development-Basics)

**ABP Studio Documentation**: [https://docs.abp.io/en/abp/latest/studio](https://docs.abp.io/en/abp/latest/studio)

**ABP Community**:

- Forum: [https://community.abp.io](https://community.abp.io)
- GitHub: [https://github.com/abpframework/abp](https://github.com/abpframework/abp)
- Sample Projects: [https://docs.abp.io/en/abp/latest/Samples/Index](https://docs.abp.io/en/abp/latest/Samples/Index)

### ABP Studio Usage

**Access**: Solution Architect and Senior Developer have accounts

**Common Tasks**:

- Create new modules: `ABP Suite > New Module`
- Generate CRUD pages: Entity scaffolding
- Manage solution structure: Add/remove modules
- Database migrations: Run and manage migrations

**Login**: Use licensed email credentials provided by Solution Architect

### Version Information

**Current ABP Version**: Check `global.json` in repository root

**Upgrade Process**:

- Review release notes: [https://github.com/abpframework/abp/releases](https://github.com/abpframework/abp/releases)
- Test in dev environment
- Coordinate upgrade across all microservices
- Document breaking changes

---

## PSPDF / Nutrient PDF Platform

### License Information

**License Type**: Yearly subscription  
**License Holder**: Yas Holding Technology - YHT EdTech Division  
**Contract Includes**: PSPDF SDK + GDPicture library  
**Renewal**: Annual  
**Managed By**: Product Manager (contract), Solution Architect (technical)

### What is Nutrient (formerly PSPDFKit)?

Nutrient provides PDF viewing, editing, and processing capabilities. Kinana uses it in the **Library sub-app** for:

- **Frontend**: PDF viewer with annotation tools
- **Backend**: PDF processing, optimization, text/image extraction

### Components Used

#### Frontend (Angular)

**PDF Viewer SDK**:

- Render PDFs in browser
- Annotation tools (highlight, comment, draw)
- Form filling
- Search within PDFs
- Print and download

**Integration**: Angular component wrapper for Nutrient SDK

#### Backend (C# / ABP.io)

**PDF Processing**:

- Text extraction (search indexing)
- Image extraction
- PDF optimization (reduce file size)
- PDF/A conversion (archival format)
- Watermarking

### Documentation Links

**Main Documentation**: [https://www.nutrient.io/guides/](https://www.nutrient.io/guides/)

**Platform-Specific Guides**:

- Web SDK: [https://www.nutrient.io/guides/web/](https://www.nutrient.io/guides/web/)
- Angular Integration: [https://www.nutrient.io/guides/web/angular/](https://www.nutrient.io/guides/web/angular/)
- Server SDK (.NET): [https://www.nutrient.io/guides/server/dotnet/](https://www.nutrient.io/guides/server/dotnet/)

**API Reference**:

- Web API: [https://www.nutrient.io/api/web/](https://www.nutrient.io/api/web/)
- Server API: [https://www.nutrient.io/api/server/dotnet/](https://www.nutrient.io/api/server/dotnet/)

**Knowledge Base**:

- [https://www.nutrient.io/kb/](https://www.nutrient.io/kb/)

**Support**:

- Support Portal: Access via Nutrient account
- Email: Check contract for support email

### License Key Management

**Location**: Environment variables (not in source code)

**Frontend License**:

```typescript
// Environment configuration
export const environment = {
  pspdfLicenseKey: process.env["PSPDF_LICENSE_KEY"],
};
```

**Backend License**:

```csharp
// appsettings.json (staging/production)
{
  "Nutrient": {
    "LicenseKey": "[from environment variable]"
  }
}
```

### Common Use Cases in Kinana

1. **View Document**: User opens PDF in Library
2. **Annotate PDF**: Teacher adds comments to educational materials
3. **Extract Text**: Backend indexes PDF content for search
4. **Optimize PDF**: Reduce file size before storage
5. **Generate Thumbnail**: Create preview images for document list

---

## GDPicture Library

### License Information

**License Type**: Included with PSPDF/Nutrient contract  
**Usage**: Backend document processing  
**Renewal**: Part of annual Nutrient renewal

### What is GDPicture?

GDPicture is a document imaging SDK providing advanced image and document processing capabilities beyond standard PDF operations.

### Features Used in Kinana

**Image Processing**:

- Image extraction from PDFs
- Image optimization (compression, resize)
- Format conversion (TIFF, JPEG, PNG)
- OCR (Optical Character Recognition) - if needed

**Document Processing**:

- Multi-format support (PDF, DOCX, images)
- Barcode reading (if needed for document classification)
- Document cleanup and enhancement

### Integration

**Backend Only**: GDPicture runs on server-side processing

**Common Operations**:

```csharp
// Example: Extract images from PDF
var gdPicture = new GdPictureImaging();
var pdfDocument = new GdPicturePDF();
pdfDocument.LoadFromFile(filePath);

for (int page = 1; page <= pdfDocument.GetPageCount(); page++)
{
    pdfDocument.SelectPage(page);
    var imageIds = pdfDocument.GetPageImageIDs();
    // Process each image
}
```

### Documentation Links

**Main Documentation**: [https://www.gdpicture.com/guides/](https://www.gdpicture.com/guides/)

**API Reference**: [https://www.gdpicture.com/documentation/](https://www.gdpicture.com/documentation/)

**Code Samples**: Included with Nutrient documentation package

### Use Cases in Kinana

1. **Text Extraction**: Extract text from scanned PDFs (OCR)
2. **Image Optimization**: Reduce image size in uploaded documents
3. **Format Conversion**: Convert uploaded images to PDF
4. **Quality Enhancement**: Clean up scanned documents

---

## Technology Documentation

### Angular

**Official Documentation**: [https://angular.io/docs](https://angular.io/docs)

**Key Sections**:

- Fundamentals: [https://angular.io/guide/architecture](https://angular.io/guide/architecture)
- Components: [https://angular.io/guide/component-overview](https://angular.io/guide/component-overview)
- Services: [https://angular.io/guide/architecture-services](https://angular.io/guide/architecture-services)
- Routing: [https://angular.io/guide/router](https://angular.io/guide/router)
- HTTP Client: [https://angular.io/guide/http](https://angular.io/guide/http)

**Style Guide**: [https://angular.io/guide/styleguide](https://angular.io/guide/styleguide)

### TypeScript

**Official Documentation**: [https://www.typescriptlang.org/docs/](https://www.typescriptlang.org/docs/)

**Handbook**: [https://www.typescriptlang.org/docs/handbook/intro.html](https://www.typescriptlang.org/docs/handbook/intro.html)

### .NET / C#

**Microsoft .NET Documentation**: [https://docs.microsoft.com/en-us/dotnet/](https://docs.microsoft.com/en-us/dotnet/)

**C# Guide**: [https://docs.microsoft.com/en-us/dotnet/csharp/](https://docs.microsoft.com/en-us/dotnet/csharp/)

**ASP.NET Core**: [https://docs.microsoft.com/en-us/aspnet/core/](https://docs.microsoft.com/en-us/aspnet/core/)

### Docker

**Official Documentation**: [https://docs.docker.com/](https://docs.docker.com/)

**Docker Desktop**: [https://docs.docker.com/desktop/](https://docs.docker.com/desktop/)

**Best Practices**: [https://docs.docker.com/develop/dev-best-practices/](https://docs.docker.com/develop/dev-best-practices/)

### Kubernetes

**Official Documentation**: [https://kubernetes.io/docs/](https://kubernetes.io/docs/)

**Tutorials**: [https://kubernetes.io/docs/tutorials/](https://kubernetes.io/docs/tutorials/)

**kubectl Cheat Sheet**: [https://kubernetes.io/docs/reference/kubectl/cheatsheet/](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)

### Azure

**Azure Documentation**: [https://docs.microsoft.com/en-us/azure/](https://docs.microsoft.com/en-us/azure/)

**Azure Kubernetes Service (AKS)**: [https://docs.microsoft.com/en-us/azure/aks/](https://docs.microsoft.com/en-us/azure/aks/)

**Azure CLI Reference**: [https://docs.microsoft.com/en-us/cli/azure/](https://docs.microsoft.com/en-us/cli/azure/)

---

## Training Materials

### Internal Training

**Onboarding Documentation**: Repository `kinana-docs/onboarding/`

**Architecture Overview**: Repository `kinana-docs/architecture/`

**Code Walkthroughs**: Either recorded during sprint reviews / handovers (Teams recordings) or in person walkthroughs with Solution Architect

### External Courses

#### ABP.io

- **ABP.io Mastery Course**: [https://abp.io/courses](https://abp.io/courses)
- **YouTube Channel**: [https://www.youtube.com/@Volosoft](https://www.youtube.com/@Volosoft)

#### Angular

- **Angular University**: [https://angular-university.io/](https://angular-university.io/)
- **Official Tutorial**: [https://angular.io/tutorial](https://angular.io/tutorial)

#### Microservices Architecture

- **Microsoft Microservices Guide**: [https://docs.microsoft.com/en-us/dotnet/architecture/microservices/](https://docs.microsoft.com/en-us/dotnet/architecture/microservices/)
- **Martin Fowler Articles**: [https://martinfowler.com/microservices/](https://martinfowler.com/microservices/)

#### Kubernetes

- **Kubernetes Basics**: [https://kubernetes.io/docs/tutorials/kubernetes-basics/](https://kubernetes.io/docs/tutorials/kubernetes-basics/)
- **Azure AKS Workshop**: [https://docs.microsoft.com/en-us/learn/paths/intro-to-kubernetes-on-azure/](https://docs.microsoft.com/en-learn/paths/intro-to-kubernetes-on-azure/)

### Community Resources

**Stack Overflow**:

- [ABP.io Questions](https://stackoverflow.com/questions/tagged/abp)
- [Angular Questions](https://stackoverflow.com/questions/tagged/angular)

**Reddit**:

- r/dotnet
- r/Angular2
- r/kubernetes

**Blogs**:

- ABP Community Blog: [https://community.abp.io/posts](https://community.abp.io/posts)
- Angular Blog: [https://blog.angular.io/](https://blog.angular.io/)

---

## License Compliance

### Usage Guidelines

**ABP.io**:

- Multi-developer license covers all team members
- Code generated by ABP Studio is covered under license
- Do not share license keys publicly (GitHub, public docs)

**PSPDF/Nutrient + GDPicture**:

- Licensed for Kinana platform use only
- Do not redistribute SDKs or license keys
- Annual renewal required for continued use and updates

### License Audit Preparation

**Documentation**:

- License agreements stored in YHT legal repository
- License keys in secure environment variable storage
- Usage tracked in this documentation

**Compliance**:

- All developers aware of license terms
- No unauthorized use in other projects
- Annual review during license renewal

---

## Support Contacts

### ABP.io Support

**Method**: Community forum, paid support ticket system  
**Access**: Solution Architect has support account  
**Response Time**: Per support tier in contract

### Nutrient Support

**Method**: Support portal (via Nutrient account)  
**Access**: Solution Architect and Product Manager have accounts  
**Response Time**: Per SLA in contract

### Azure Support

**Method**: Azure Portal support tickets  
**Access**: Solution Architect (owner role)  
**Support Plan**: Per YHT corporate Azure agreement

---

## Resource Updates

### Staying Current

**Release Notes**:

- ABP.io: [https://github.com/abpframework/abp/releases](https://github.com/abpframework/abp/releases)
- Nutrient: Check support portal for announcements
- Angular: [https://github.com/angular/angular/releases](https://github.com/angular/angular/releases)

**Security Updates**:

- Subscribe to security mailing lists for critical frameworks
- Review CVE databases for known vulnerabilities
- Apply patches promptly

### Documentation Maintenance

**Responsibility**: Solution Architect updates this document when:

- New licenses acquired
- Documentation URLs change
- New training resources identified
- Support contacts updated

---

_Last Updated: November 2025_  
_Version: 1.0_
