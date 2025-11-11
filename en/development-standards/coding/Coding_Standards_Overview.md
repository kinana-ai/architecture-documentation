# Coding Standards - Overview

## Purpose

Coding standards ensure consistency and maintainability across Kinana's multi-language codebase. These standards reference authoritative external guides and establish Kinana-specific conventions where needed.

---

## Guiding Principles

**1. Readability First**
Code is read more often than written. Optimize for clarity.

**2. Consistency Over Personal Preference**
Follow established patterns in the codebase. Match surrounding code style.

**3. Self-Documenting Code**
- Choose descriptive names
- Keep functions focused and small
- Extract complex logic into well-named functions
- Comments explain *why*, not *what*

**4. DRY (Don't Repeat Yourself)**
Extract reusable code into shared functions, components, or services.

**5. YAGNI (You Aren't Gonna Need It)**
Don't build features or abstractions before they're needed.

---

## Language-Specific Standards

### JavaScript / TypeScript (Angular Frontend)

**Primary Reference**: [Angular Style Guide](https://angular.io/guide/styleguide) (official)

**Key Standards**:
- Follow Angular CLI scaffolding conventions
- One component/service per file
- Use TypeScript strict mode
- Prefer interfaces over classes for data models
- Use RxJS operators for reactive programming
- Async/await preferred over promise chains

**Detailed Guide**: [JavaScript Style Guide](./Coding_Standards_JavaScript.md)

---

### C# / .NET (ABP.io Backend)

**Primary References**: 
- [C# Coding Conventions](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/coding-style/coding-conventions) (Microsoft official)
- [ABP Best Practices](https://docs.abp.io/en/abp/latest/Best-Practices/Index) (framework-specific)

**Key Standards**:
- Follow ABP Framework conventions and patterns
- Domain-Driven Design (DDD) layer separation
- Use dependency injection (built into ABP)
- Async/await for I/O operations
- LINQ for data queries

**Detailed Guide**: [C# Style Guide](./Coding_Standards_CSharp.md)

---

### Python (AI Development)

**Primary Reference**: [PEP 8](https://peps.python.org/pep-0008/) (official Python style guide)

**Key Standards**:
- Follow PEP 8 conventions
- Use virtual environments
- Type hints for function signatures
- Docstrings for modules and functions
- Keep scripts modular and reusable

**Detailed Guide**: [Python Style Guide](./Coding_Standards_Python.md)

---

## Cross-Language Standards

### Naming Conventions

**Consistency across languages** with language-specific casing:

- **Files/Components**: Match language conventions
- **Functions/Methods**: Descriptive, verb-based names
- **Variables**: Descriptive nouns
- **Constants**: Uppercase with underscores (Python, TypeScript) or PascalCase (C#)
- **Booleans**: Prefixed with is/has/can/should

**Detailed Guide**: [Naming Conventions](./Coding_Standards_Naming.md)

---

### Best Practices

**Universal principles** applicable across all languages:

- **Error Handling**: Always handle errors gracefully
- **Security**: Input validation, output encoding, secure authentication
- **Performance**: Avoid premature optimization, but don't be wasteful
- **Maintainability**: Code should be easy to modify and extend
- **Testing**: Write code that's testable (even if not writing tests yet)

**Detailed Guide**: [Best Practices](./Coding_Standards_BestPractices.md)

---

## Automated Enforcement

### Linting & Formatting

**Frontend (Angular/TypeScript)**:
```json
// .eslintrc.json
{
  "extends": [
    "plugin:@angular-eslint/recommended",
    "plugin:@typescript-eslint/recommended"
  ]
}
```

**Prettier** (auto-formatting):
```json
// .prettierrc
{
  "singleQuote": true,
  "trailingComma": "es5",
  "printWidth": 100,
  "tabWidth": 2
}
```

**Backend (C#)**:
- Roslyn analyzers (built into .NET SDK)
- EditorConfig for consistent formatting
- StyleCop (optional, for stricter enforcement)

**Python**:
- pylint or flake8 for linting
- black for auto-formatting
- mypy for type checking

### VS Code Integration

**Recommended Extensions**:
- ESLint
- Prettier
- C# (OmniSharp)
- Python (Microsoft)
- EditorConfig

**Settings** (workspace):
```json
{
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "[csharp]": {
    "editor.defaultFormatter": "ms-dotnettools.csharp"
  },
  "[python]": {
    "editor.defaultFormatter": "ms-python.black-formatter"
  }
}
```

---

## Code Review Focus

### What to Check
✓ Follows language-specific style guide  
✓ Naming is clear and consistent  
✓ No obvious bugs or logic errors  
✓ Error handling present  
✓ No security vulnerabilities  
✓ Performance considerations appropriate  

### What Not to Obsess Over
✗ Minor style differences (if auto-formatted)  
✗ Personal preferences (if both approaches valid)  
✗ Micro-optimizations without evidence  
✗ Over-engineering for hypothetical futures  

---

## When to Deviate

Standards are guidelines, not laws. Deviate when:
- Performance requires it (document why)
- Third-party integration demands it
- Existing codebase pattern established
- Team consensus on better approach

**Rule**: Document significant deviations with comments explaining rationale.

---

## Resources

### Official Language Documentation
- **TypeScript**: https://www.typescriptlang.org/docs/
- **Angular**: https://angular.io/docs
- **C# / .NET**: https://learn.microsoft.com/en-us/dotnet/
- **ABP Framework**: https://docs.abp.io/
- **Python**: https://docs.python.org/

### Style Guides
- **Angular Style Guide**: https://angular.io/guide/styleguide
- **C# Coding Conventions**: https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/coding-style/coding-conventions
- **PEP 8 (Python)**: https://peps.python.org/pep-0008/
- **Airbnb JavaScript Style Guide**: https://github.com/airbnb/javascript (reference)
- **Google Style Guides**: https://google.github.io/styleguide/ (reference)

### Tools
- **Prettier**: https://prettier.io/
- **ESLint**: https://eslint.org/
- **Roslyn Analyzers**: Built into .NET SDK
- **Black (Python)**: https://black.readthedocs.io/

---

*Last Updated: November 2025*  
*Version: 1.0*  
*Standards reference external authoritative sources and are enforced through code review and automated tools*
