# Architecture Diagrams

This directory contains professional SVG diagrams illustrating the Kinana Platform architecture. All diagrams are scalable vector graphics that can be viewed in any modern web browser or embedded in documentation.

## Available Diagrams

### System Architecture

#### 1. **layer-architecture.svg** (800×600px)
**Used in**: [02-System-Architecture.md](02-System-Architecture.md)

Visual representation of the 6-layer platform architecture:
- Layer 1: Internet / Users
- Layer 2: Ingress & TLS Termination (NGINX)
- Layer 3: Core Services (Identity, API, Admin)
- Layer 4: Application Services (PDF, Document Mgmt, Translation, LTI, Web Apps)
- Layer 5: Data Layer (Redis, MySQL, SQL Server)
- Layer 6: Storage Layer (Azure Blob Storage)

---

#### 2. **microservices-overview.svg** (1000×700px)
**Used in**: [02-System-Architecture.md](02-System-Architecture.md)

Comprehensive view of all 20+ microservices organized by function:
- Core Services (3 services)
- Application Services (4+ services)
- PDF Processing Services (4 services)
- LTI Integration Services (2 services)
- Data Layer (3 data stores)
- Storage Layer with platform statistics

---

#### 3. **service-communication.svg** (800×500px)
**Used in**: [02-System-Architecture.md](02-System-Architecture.md)

Illustrates service-to-service communication patterns:
- Shared Redis cache access across services
- Internal MySQL database connections
- External SQL Server connections (LTI)
- Kubernetes DNS service discovery

---

### Data Architecture

#### 4. **three-tier-storage.svg** (700×450px)
**Used in**: [03-Data-Architecture-Overview.md](03-Data-Architecture-Overview.md)

Clean three-tier storage model diagram:
- Tier 1: Cache Layer (Redis) - HOT, ~1ms
- Tier 2: Database Layer (MySQL, SQL Server) - WARM, ~10ms
- Tier 3: Blob Storage (Azure) - COLD, ~100ms

---

#### 5. **three-tier-storage-detailed.svg** (800×550px)
**Used in**: [05-Data-Architecture.md](05-Data-Architecture.md)

Detailed three-tier storage model with comprehensive information:
- Performance characteristics for each tier
- Access patterns and persistence details
- Purpose and use cases
- Storage capacity and features

---

### Security Architecture

#### 6. **defense-in-depth.svg** (700×550px)
**Used in**: [08-Security-Architecture.md](08-Security-Architecture.md)

Defense in Depth multi-layer security strategy:
- Layer 7: User Awareness & Training
- Layer 6: Application Security
- Layer 5: Data Security
- Layer 4: Network Security
- Layer 3: Host Security
- Layer 2: Infrastructure Security
- Layer 1: Policies & Procedures

---

#### 7. **zero-trust-flow.svg** (500×650px)
**Used in**: [08-Security-Architecture.md](08-Security-Architecture.md)

Zero Trust security model flow:
1. Request received
2. Authentication (Who are you?)
3. Authorization (What can you do?)
4. Context Evaluation (Is this normal?)
5. Continuous Verification (Monitor throughout session)

---

### Integration Architecture

#### 8. **lti-architecture.svg** (800×400px)
**Used in**: [11-Integration-Architecture.md](11-Integration-Architecture.md)

LTI 1.3 integration architecture:
- LMS Platform connection via OIDC
- Kinana LTI Service (xwinji, readerapp)
- Kinana Application with JWT tokens
- SQL Server database for LTI state

---

## Technical Specifications

### SVG Format Details
- **Format**: SVG 1.1 (Scalable Vector Graphics)
- **Compatibility**: All modern browsers
- **File Sizes**: 3-8 KB per diagram
- **Scalability**: Infinite (vector-based)
- **Fonts**: Arial, sans-serif (web-safe)
- **Color Palette**: Consistent across diagrams

### Color Scheme

| Component Type | Color Code | Usage |
|----------------|------------|-------|
| Layer 1 (Purple) | #667eea | User/Internet layer, Core services |
| Layer 2 (Dark Purple) | #764ba2 | Ingress layer |
| Layer 3 (Pink) | #f093fb | Core services, LTI |
| Layer 4 (Blue) | #4facfe | Application services |
| Layer 5 (Green) | #43e97b | Data layer |
| Layer 6 (Coral) | #fa709a | Storage layer |
| Database (Green) | #50C878 | Database components |
| Cache (Red) | #FF6B6B | Redis cache |
| Security (Green gradient) | #43A047-#E8F5E9 | Security layers |

---

## Viewing the Diagrams

### Option 1: In Web Browser
Simply open any `.svg` file in your browser:
```bash
open layer-architecture.svg
# or
firefox microservices-overview.svg
```

### Option 2: In Markdown
Diagrams are embedded in documentation using:
```markdown
![Diagram Description](diagram-name.svg)
```

### Option 3: In HTML/Web Pages
```html
<img src="layer-architecture.svg" alt="Layer Architecture">
<!-- or -->
<object data="layer-architecture.svg" type="image/svg+xml"></object>
```

### Option 4: Image Viewers
Any SVG-compatible image viewer can display these diagrams.

---

## Editing the Diagrams

### Recommended Tools
- **Vector Editors**: Adobe Illustrator, Inkscape (free), Figma
- **Code Editors**: VS Code, Sublime Text (edit XML directly)
- **Online Tools**: Vectr, SVG-edit

### Editing Process
1. Open the `.svg` file in your preferred editor
2. Modify the XML/SVG code or use visual tools
3. Save the file
4. Preview in a browser to verify changes
5. Update documentation if diagram content changed significantly

### SVG Structure
Each diagram follows a standard structure:
```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600">
  <defs>
    <style>/* CSS styles */</style>
    <marker>/* Arrow definitions */</marker>
  </defs>
  
  <!-- Title -->
  <text>...</text>
  
  <!-- Diagram elements -->
  <rect>...</rect>
  <path>...</path>
  <text>...</text>
</svg>
```

---

## Updating Diagrams

### When to Update
- Architecture changes (new services, components)
- Technology stack updates
- Process flow modifications
- Rebranding or style updates

### Update Checklist
- [ ] Update the SVG file with new information
- [ ] Verify diagram renders correctly in browser
- [ ] Update documentation that references the diagram
- [ ] Check that colors and fonts are consistent
- [ ] Test on different screen sizes/browsers
- [ ] Commit changes to version control

---

## Design Guidelines

### Consistency
- Use the established color palette
- Maintain consistent box sizes within diagram types
- Use the same fonts (Arial, sans-serif)
- Keep arrow styles uniform

### Clarity
- Ensure text is readable at various zoom levels
- Use appropriate font sizes (title: 20-24px, body: 12-16px)
- Maintain adequate spacing between elements
- Include labels for all connections

### Accessibility
- Use sufficient color contrast
- Include alt text when embedding in HTML
- Ensure diagrams work in grayscale (printability)

---

## Advantages of SVG

✅ **Scalable**: No quality loss at any zoom level
✅ **Small File Size**: 3-8 KB per diagram vs 50-200 KB for PNG
✅ **Editable**: Can be modified with text editors or design tools
✅ **Searchable**: Text content is selectable and searchable
✅ **Accessible**: Screen readers can access text content
✅ **Print-Friendly**: Crisp output at any print resolution
✅ **Web-Optimized**: Fast loading, supported by all modern browsers

---

## Integration with Documentation

All diagrams are directly embedded in the corresponding markdown documentation files. The diagrams enhance understanding by:

1. **Visual Learning**: Complex architectures made easy to understand
2. **Quick Reference**: Instant overview of system components
3. **Professional Presentation**: Clean, consistent visual style
4. **Maintenance**: Easy to update when architecture evolves

---

## Future Diagram Plans

Planned diagrams for future releases:
- [ ] Data Flow Diagrams (file upload, retrieval, processing)
- [ ] Network Topology Diagram
- [ ] Deployment Pipeline Diagram
- [ ] Authentication Flow Diagrams
- [ ] Database Entity Relationship Diagrams
- [ ] Disaster Recovery Flow
- [ ] Monitoring Architecture

---

## Summary

| Diagram | Size | Used In | Focus Area |
|---------|------|---------|------------|
| layer-architecture.svg | 800×600 | System Arch | 6-layer platform structure |
| microservices-overview.svg | 1000×700 | System Arch | All 20+ microservices |
| service-communication.svg | 800×500 | System Arch | Service interactions |
| three-tier-storage.svg | 700×450 | Data Arch Overview | Storage tiers (simple) |
| three-tier-storage-detailed.svg | 800×550 | Data Arch | Storage tiers (detailed) |
| defense-in-depth.svg | 700×550 | Security Arch | 7 security layers |
| zero-trust-flow.svg | 500×650 | Security Arch | Zero trust process |
| lti-architecture.svg | 800×400 | Integration Arch | LTI 1.3 flow |

**Total**: 8 professional SVG diagrams | 33 KB total size

---

**Version**: 1.0  
**Last Updated**: November 19, 2024  
**Format**: SVG (Scalable Vector Graphics)  
**License**: Proprietary - YHT EdTech Division
