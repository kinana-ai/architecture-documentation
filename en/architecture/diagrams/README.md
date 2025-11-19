# Kinana Platform Architecture Diagrams

This directory contains visual architecture diagrams for the Kinana Platform. All diagrams are created in SVG format for scalability and quality.

## 📊 Available Diagrams

### 1. Layer Architecture (`layer-architecture.svg`)
**Dimensions**: 800x600px

Visual representation of the 6-layer architecture:
- Layer 1: Internet / Users
- Layer 2: Ingress & TLS Termination
- Layer 3: Core Services
- Layer 4: Application Services
- Layer 5: Data Layer
- Layer 6: Storage Layer

**Usage**: Shows the high-level architectural layers and data flow through the system.

---

### 2. Microservices Overview (`microservices-overview.svg`)
**Dimensions**: 1000x700px

Comprehensive view of all microservices organized by function:
- Core Services (3 services)
- Application Services (4+ services)
- PDF Processing Services (4 services)
- LTI Integration Services (2 services)
- Data Layer (3 data stores)
- Storage Layer (Azure Blob Storage)

**Usage**: Provides a complete picture of all services, their domains, and organization.

---

### 3. Service Communication (`service-communication.svg`)
**Dimensions**: 800x500px

Illustrates how services communicate with each other:
- Shared Redis cache access
- Internal database connections
- External database connections (LTI)
- Kubernetes DNS service discovery

**Usage**: Understanding service dependencies and communication patterns.

---

## 🖼️ Viewing the Diagrams

### Option 1: HTML Viewer (Recommended)
Open `index.html` in your web browser for an interactive viewing experience with:
- Navigation between diagrams
- Descriptions and context
- Responsive design
- Key features and statistics

```bash
# Open in default browser
open index.html
# or
firefox index.html
# or
chrome index.html
```

### Option 2: Direct SVG View
Open any `.svg` file directly in your browser:
```bash
open layer-architecture.svg
```

### Option 3: Markdown Embedding
SVG files are embedded in the documentation using:
```markdown
![Diagram Description](diagrams/filename.svg)
```

### Option 4: Image Viewers
Any image viewer that supports SVG format can display these diagrams.

---

## 🎨 Diagram Color Scheme

| Component Type | Color | Usage |
|----------------|-------|-------|
| **Layer 1** | Purple (#667eea) | User/Internet layer |
| **Layer 2** | Dark Purple (#764ba2) | Ingress layer |
| **Layer 3** | Pink (#f093fb) | Core services |
| **Layer 4** | Blue (#4facfe) | Application services |
| **Layer 5** | Green (#43e97b) | Data layer |
| **Layer 6** | Coral (#fa709a) | Storage layer |
| **Core Services** | Purple (#667eea) | Identity, API, Admin |
| **App Services** | Sky Blue (#4facfe) | Application microservices |
| **PDF Services** | Pink Gradient (#fa709a-#fee140) | PDF processing |
| **LTI Services** | Purple-Blue (#f093fb) | LTI integration |
| **Data Services** | Green (#50C878) | Databases |
| **Cache** | Red (#FF6B6B) | Redis cache |

---

## 📐 Technical Details

### SVG Specifications
- **Format**: SVG 1.1
- **Compatibility**: All modern browsers
- **Scalability**: Vector format (infinite scaling)
- **File Size**: 3-8 KB per diagram
- **Fonts**: Arial, sans-serif (web-safe)

### Editing Diagrams
These SVG files can be edited with:
- **Vector Editors**: Adobe Illustrator, Inkscape, Figma
- **Code Editors**: VS Code, Sublime Text (XML editing)
- **Online Tools**: SVG-edit, Vectr

To modify:
1. Open the `.svg` file in your preferred editor
2. Modify the XML/SVG code or use visual tools
3. Save and preview in a browser
4. Update the documentation if diagram content changes

---

## 🔄 Updating Diagrams

When architecture changes:

1. **Update the SVG file** with new information
2. **Update the HTML viewer** (`index.html`) descriptions if needed
3. **Update documentation** that references the diagram
4. **Test in browser** to ensure proper rendering
5. **Commit changes** to version control

---

## 📱 Responsive Design

The HTML viewer (`index.html`) is fully responsive and works on:
- Desktop computers (1920x1080+)
- Laptops (1366x768+)
- Tablets (768x1024+)
- Mobile devices (320x568+)

SVG diagrams automatically scale to fit the container while maintaining aspect ratio.

---

## 🔗 Related Documentation

- [System Architecture Document](../02-System-Architecture.md) - Uses all three diagrams
- [Platform Architecture Overview](../01-Platform-Architecture-Overview.md) - References layer architecture
- [README](../README.md) - Main documentation index

---

## 📝 Diagram Version History

| Date | Version | Changes |
|------|---------|---------|
| 2024-11-19 | 1.0 | Initial creation of all three diagrams |

---

## 💡 Tips for Best Viewing

1. **Use a modern browser** (Chrome, Firefox, Safari, Edge) for best SVG rendering
2. **Zoom capabilities**: SVGs can be zoomed without quality loss
3. **Print-friendly**: Diagrams print clearly at any size
4. **Dark mode**: Consider viewing in light mode for best contrast
5. **Screen size**: Larger screens provide better overview

---

## 🎯 Future Diagram Plans

Planned diagrams for future releases:
- [ ] Data Flow Diagrams (file upload, retrieval, processing)
- [ ] Security Architecture Diagram
- [ ] Network Topology Diagram
- [ ] Deployment Pipeline Diagram
- [ ] LTI Integration Flow Diagram
- [ ] Authentication Flow Diagram
- [ ] Database Schema Diagram

---

## 📧 Feedback

For questions, corrections, or suggestions about these diagrams:
1. Review the diagram accuracy against actual implementation
2. Check if updates are needed due to architecture changes
3. Suggest improvements for clarity or detail
4. Report any rendering issues

---

**Created**: November 19, 2024  
**Version**: 1.0  
**Format**: SVG (Scalable Vector Graphics)  
**License**: Proprietary - YHT EdTech Division
