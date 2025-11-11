# Source Documentation Standards - Overview

## Philosophy

**Code is King**: Well-written code is self-documenting. Documentation supplements code, not replaces it.

**Senior Team**: These standards assume experienced developers who understand when and why to document, not how to write code.

---

## Documentation Principles

### 1. Document WHY, Not WHAT

Code shows what it does. Comments explain why it does it.

### 2. Self-Documenting Code First

- Descriptive names > comments
- Small focused functions > lengthy explanations
- Clear structure > documentation

### 3. Required Documentation Only

- Copyright headers (all files)
- Public APIs (interfaces, services)
- Complex algorithms (business logic)
- Non-obvious decisions (trade-offs, workarounds)

### 4. Keep It Current

Outdated documentation is worse than no documentation. If code changes, update docs or remove them.

---

## Documentation Scope

### Code Documentation

Inline comments, function/method documentation, and code-level explanations.

**Key Areas**:

- Commenting standards (when and how)
- Documentation requirements (what must be documented)
- Documentation tools (JSDoc, XML docs, docstrings)

### File Header Standards

Standardized headers for copyright, license, and attribution.

**Key Areas**:

- Copyright header template (required on all source files)
- License information
- Author attribution
- File-level documentation

### Technical Documentation

README files and API documentation for external consumption.

**Key Areas**:

- README standards (repository documentation)
- API documentation (for integrations)
- Architecture documentation (high-level design)

---

## Documentation by Role

### Frontend (Angular/TypeScript)

- **Required**: Copyright headers, public API documentation
- **Tools**: JSDoc for public APIs, inline comments sparingly
- **Focus**: Component interfaces, service APIs

### Backend (C# / ABP.io)

- **Required**: Copyright headers, XML documentation for public APIs
- **Tools**: XML documentation comments, inline comments for complex logic
- **Focus**: Application service interfaces, domain models, APIs

### Python (AI Development)

- **Required**: Copyright headers, module/function docstrings
- **Tools**: Python docstrings (Google/NumPy style)
- **Focus**: Function signatures, module purpose, algorithm explanations

---

## Documentation Standards

### Source Code Documentation

**[Code Documentation Standards](./code-documentation/Code_Documentation_Standards.md)**

- When to comment
- Documentation requirements
- Tools and formats

### File Headers

**[File Header Standards](./file-headers/File_Header_Standards.md)**

- Copyright header template (required)
- License information
- Author attribution

---

## Anti-Patterns

**Don't Do This**:

```typescript
// ❌ Bad - states the obvious
// Increment counter
counter++;

// ❌ Bad - outdated comment
// TODO: Refactor this (from 2 years ago, already refactored)

// ❌ Bad - commented-out code
// const oldFunction = () => { ... }

// ❌ Bad - redundant documentation
/**
 * Gets the user name
 * @returns the user name
 */
getUserName(): string { }
```

**Do This**:

```typescript
// ✅ Good - explains WHY
// Retry 3 times because API occasionally returns 502 during deployments
retry(3)

// ✅ Good - documents non-obvious business logic
// VAT applies to EU customers only, except for business accounts with valid VAT ID
if (isEuCustomer && (!isBusinessAccount || !hasValidVatId)) {
  applyVat = true;
}

// ✅ Good - useful API documentation
/**
 * Retrieves user profile with role information.
 * Throws EntityNotFoundException if user not found.
 */
getUserProfile(userId: string): Observable<UserProfile>
```

---

## External Standards

Rather than duplicate, we reference:

**JavaScript/TypeScript**:

- JSDoc: https://jsdoc.app/
- TSDoc: https://tsdoc.org/

**C# / .NET**:

- XML Documentation: https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/xmldoc/

**Python**:

- PEP 257 (Docstrings): https://peps.python.org/pep-0257/
- Google Python Style Guide: https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings

---

## Enforcement

**Code Review**: Primary enforcement mechanism

- Reviewers check for required copyright headers
- Verify public APIs are documented
- Flag misleading or outdated comments

**Automated**: Linters catch missing documentation (configurable)

---

_Last Updated: November 2025_  
_Version: 1.0_
