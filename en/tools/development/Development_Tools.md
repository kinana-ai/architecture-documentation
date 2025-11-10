# Development Tools

## Overview

Kinana development is standardized on Visual Studio Code running on Windows 10/11 workstations, with specialized environments for infrastructure access, AI development, and future mobile development.

---

## IDE Setup

### Visual Studio Code

**Version**: Latest stable release  
**Platform**: Windows 10/11 (primary), macOS (infrastructure team)

#### Installation

1. Download from [code.visualstudio.com](https://code.visualstudio.com)
2. Install with default options
3. Configure GitHub authentication
4. Install required extensions (see Plugins & Extensions section)

#### Workspace Configuration

**Recommended Settings** (`.vscode/settings.json`):

```json
{
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.codeActionsOnSave": {
    "source.fixAll.eslint": true
  },
  "files.autoSave": "onFocusChange",
  "typescript.preferences.importModuleSpecifier": "relative"
}
```

#### Multi-Root Workspaces

Given Kinana's many repositories:

- Use VS Code multi-root workspaces for related components
- Example workspace file: `kinana-workspace.code-workspace`
- Group by sub-app: Shell, Library, Videos, Podcasts, Brokkly

#### Integrated Terminal

- **Default Shell**: PowerShell (Windows) or Bash (macOS/Linux)
- **Common Commands**: npm, Angular CLI, ABP CLI, Docker commands
- **Split Terminals**: Multiple terminals for frontend/backend simultaneous development

---

## Plugins & Extensions

### Essential Extensions

#### Code Quality & Formatting

**Prettier - Code formatter** (`esbenp.prettier-vscode`)

- Enforces consistent code style
- Configured in `.prettierrc` files in each repository
- Auto-formats on save

**ESLint** (`dbaeumer.vscode-eslint`)

- JavaScript/TypeScript linting
- Catches errors during development
- Integrates with Angular projects

**C# Dev Kit** (Microsoft)

- Backend C# development support
- IntelliSense and debugging for ABP.io code

#### Language Support

**Angular Language Service** (Angular)

- Template type checking
- Auto-completion in Angular templates
- Navigation to components and services

**C# Extensions** (`ms-dotnettools.csharp`)

- Full C# language support
- Required for ABP.io backend development

#### Documentation & Markdown

**Markdown All in One** (`yzhang.markdown-all-in-one`)

- Markdown editing with preview
- Table of contents generation
- Used for README and technical documentation

**Markdown Preview Enhanced** (optional)

- Enhanced markdown preview with diagrams
- Export to PDF/HTML

#### Web Development

**HTML CSS Support** (`ecmel.vscode-html-css`)

- CSS class name completion in HTML
- Supports Angular templates

**Auto Rename Tag** (`formulahendry.auto-rename-tag`)

- Automatically renames paired HTML/XML tags
- Improves HTML/Angular template editing efficiency

#### Version Control

**GitLens** (`eamodio.gitlens`)

- Enhanced Git capabilities
- Blame annotations, commit history
- Helps understand code evolution

**GitHub Pull Requests** (GitHub)

- Manage PRs directly from VS Code
- Review code without leaving editor

#### Docker Support

**Docker** (Microsoft)

- Docker file syntax highlighting
- Build, manage, and deploy containers
- Essential for local microservices development

#### Utilities

**Path Intellisense** (`christian-kohler.path-intellisense`)

- Auto-completes file paths
- Helpful for imports and relative paths

**Bracket Pair Colorizer** (built-in to VS Code now)

- Colorizes matching brackets
- Improves readability of nested code

### Optional Extensions

- **Thunder Client**: REST API testing (alternative to Postman)
- **Live Server**: Quick HTML preview
- **Todo Tree**: Highlights TODO comments
- **Better Comments**: Color-coded comment styles

---

## Local Environment

### Required Software Stack

#### Core Development Tools

**Node.js** (LTS version)

- JavaScript runtime for Angular development
- npm package manager
- Version: Align with production environment

**Angular CLI**

```bash
npm install -g @angular/cli
```

- Scaffold components, services, modules
- Local development server
- Build and deployment tools

**.NET SDK** (Version 8.0+)

```bash
# Download from Microsoft
# Required for ABP.io backend development
```

**ABP CLI**

```bash
dotnet tool install -g Volo.Abp.Cli
```

- Generate ABP.io modules and entities
- Database migrations
- Solution management

#### Version Control

**Git for Windows**

- Command-line Git tools
- Integration with VS Code

**GitHub Desktop** (optional)

- GUI for Git operations
- Simplifies branch management and merging

**GitHub Authentication**

- SSH keys configured for repository access
- Personal access tokens for HTTPS

#### Container & Orchestration

**Docker Desktop**

- Required for local microservices development
- Builds container images
- Local Kubernetes cluster (optional)

**Windows Subsystem for Linux (WSL2)**

- Backend for Docker Desktop
- Improves container performance on Windows

### Local Folder Structure

**Recommended Organization**:

```
C:\Dev\Kinana\
├── Shell\
│   ├── frontend\
│   └── backend\
├── Library\
│   ├── frontend\
│   └── backend\
├── Videos\
│   ├── frontend\
│   └── backend\
├── Podcasts\
│   ├── frontend\
│   └── backend\
├── Brokkly\
│   ├── frontend\
│   └── backend\
└── Infrastructure\
    ├── kubernetes\
    └── docker\
```

### Local Build & Test Workflow

#### Frontend (Angular)

1. **Install Dependencies**

   ```bash
   npm install
   ```

2. **Run Development Server**

   ```bash
   ng serve
   ```

   - Accessible at `http://localhost:4200`
   - Live reload on file changes

3. **Build Production**

   ```bash
   ng build --configuration production
   ```

4. **Run Tests**
   ```bash
   ng test        # Unit tests
   ng e2e         # End-to-end tests (if configured)
   ```

#### Backend (ABP.io)

1. **Restore Packages**

   ```bash
   dotnet restore
   ```

2. **Database Migrations**

   ```bash
   dotnet ef database update
   ```

3. **Run Application**

   ```bash
   dotnet run
   ```

   - API accessible at `http://localhost:5000` or configured port

4. **Run Tests**
   ```bash
   dotnet test
   ```

#### Docker Local Testing

1. **Build Container**

   ```bash
   docker build -t kinana/service-name:local .
   ```

2. **Run Container**

   ```bash
   docker run -p 5000:5000 kinana/service-name:local
   ```

3. **Docker Compose** (for multi-service testing)
   ```bash
   docker-compose up
   ```

### GitHub Integration

#### Clone Repository

Using GitHub CLI:

```bash
gh repo clone kinana-ai/ai.kinana.common
```

Or using Git:

```bash
git clone git@github.com:kinana-ai/ai.kinana.common.git
```

#### Local Development Branch

```bash
cd ai.kinana.common
git checkout -b feature/your-feature-name
```

#### Commit Changes

```bash
git add .
git commit -m "Descriptive commit message"
```

#### Push to GitHub

```bash
git push origin feature/your-feature-name
```

#### Sync with Remote

```bash
git pull origin dev
```

#### Switch to Dev Branch

```bash
git checkout dev
git pull origin dev
```

### Environment Configuration

**Local Development Variables**:

- Stored in `.env` files (not committed to GitHub)
- Examples: database connection strings, API keys
- Template provided in `.env.example`

**appsettings.Development.json** (Backend):

```json
{
  "ConnectionStrings": {
    "Default": "Server=localhost;Database=KinanaLocal;..."
  },
  "Azure": {
    "StorageAccount": "local-storage-emulator"
  }
}
```

---

## Debugging Tools

### VS Code Debugging

#### Frontend (Angular) Debugging

**Launch Configuration** (`.vscode/launch.json`):

```json
{
  "type": "chrome",
  "request": "launch",
  "name": "Angular Debug",
  "url": "http://localhost:4200",
  "webRoot": "${workspaceFolder}",
  "sourceMaps": true
}
```

**Workflow**:

1. Set breakpoints in TypeScript files
2. Start `ng serve`
3. Run debug configuration
4. Browser opens with debugger attached

#### Backend (ABP.io) Debugging

**Launch Configuration**:

```json
{
  "type": "coreclr",
  "request": "launch",
  "name": ".NET Core Launch",
  "preLaunchTask": "build",
  "program": "${workspaceFolder}/bin/Debug/net8.0/App.dll",
  "args": [],
  "cwd": "${workspaceFolder}",
  "stopAtEntry": false
}
```

**Workflow**:

1. Set breakpoints in C# files
2. Press F5 or Run > Start Debugging
3. Application starts with debugger attached

### Browser Developer Tools

**Chrome DevTools** (Primary)

- Network inspection for API calls
- Console for JavaScript errors
- Application tab for storage/cookies
- Performance profiling

**Angular DevTools Extension**

- Component tree visualization
- State inspection
- Performance profiling

### Docker Debugging

**Attach to Running Container**:

```bash
docker exec -it container-name /bin/bash
```

**View Logs**:

```bash
docker logs -f container-name
```

**VS Code Docker Extension**:

- Right-click container → Attach Shell
- View logs in integrated terminal

### API Testing Tools

**Built-in Swagger UI**:

- ABP.io includes Swagger by default
- Access at `http://localhost:5000/swagger`
- Test API endpoints interactively

**Thunder Client** (VS Code extension):

- REST API client within VS Code
- Save requests in workspace
- Alternative to Postman

### Database Debugging

**SQL Server Management Studio** (if using SQL Server locally):

- Query database directly
- View migrations and schema

**Azure Data Studio** (cross-platform alternative):

- Lightweight database tool
- Works with SQL Server and PostgreSQL

---

## Specialized Development Environments

### Infrastructure Access (Solution Architect / Senior Dev)

**Azure CLI**:

```bash
az login
az aks get-credentials --resource-group kinana-rg --name kinana-staging
```

**kubectl** (Kubernetes CLI):

```bash
kubectl get pods
kubectl logs pod-name
kubectl exec -it pod-name -- /bin/bash
```

### AI Development (Ubuntu Workstation)

**Hardware**: NVIDIA 4090 GPU  
**OS**: Latest Ubuntu LTS

**Software Stack**:

- CUDA Toolkit
- PyTorch or TensorFlow
- Docker for model deployment

**Usage**: Local AI model development before Azure integration

### Mobile Development (Future)

**macOS Workstations**: Solution Architect and Senior Developer

**iOS Development**:

- Xcode
- iOS Simulator
- CocoaPods or Swift Package Manager

**Android Development** (if needed):

- Android Studio
- Android emulators

**Note**: Mobile app development not yet active in Kinana but infrastructure in place.

---

## Tool Updates & Maintenance

### VS Code Updates

- Auto-update enabled by default
- Major updates reviewed by Solution Architect before team adoption

### Extension Updates

- Auto-update recommended for most extensions
- Breaking changes communicated in team standup

### Framework Updates

- Node.js, .NET SDK: Updated per sprint planning discussion
- Major version upgrades: Coordinated across team
- Angular/ABP.io versions: Align with production requirements

---

_Last Updated: November 2025_  
_Version: 1.0_
