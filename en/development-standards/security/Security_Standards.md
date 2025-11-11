# Security Standards

## Overview

Security is integrated into Kinana's development process. This document outlines secure coding practices for developers.

**Detailed Security Policies**: [Compliance & Governance - Security Compliance](../compliance/Security_Compliance.md)  
**IP Governance**: YHT SharePoint repository

---

## OWASP Top 10 Compliance

### Reference
**OWASP Top 10**: https://owasp.org/www-project-top-10/

All developers should be familiar with OWASP Top 10 vulnerabilities:

1. **Broken Access Control** - Authorization checks on all endpoints
2. **Cryptographic Failures** - Encryption for sensitive data
3. **Injection** - Input validation and parameterized queries
4. **Insecure Design** - Security by design, threat modeling
5. **Security Misconfiguration** - Secure defaults, minimal configuration
6. **Vulnerable Components** - Keep dependencies updated
7. **Authentication Failures** - Strong authentication, secure sessions
8. **Data Integrity Failures** - Verify data integrity, secure deserialization
9. **Logging Failures** - Comprehensive audit logging
10. **Server-Side Request Forgery** - Validate and sanitize URLs

---

## Secure Coding Practices

### Input Validation

**Always validate user input**:

```typescript
// ✅ Good - validate and sanitize
function createUser(input: CreateUserDto): User {
  if (!input.email || !isValidEmail(input.email)) {
    throw new ValidationError('Invalid email');
  }
  
  if (!input.name || input.name.length > 128) {
    throw new ValidationError('Invalid name');
  }
  
  const sanitizedInput = sanitizeHtml(input.bio);
  // ...
}

// ❌ Bad - no validation
function createUser(input: any): User {
  return database.create(input); // Dangerous!
}
```

**Backend validation always required** (never trust client):
```csharp
// ✅ Good - server-side validation
[Authorize]
public async Task<UserDto> CreateAsync(CreateUserDto input)
{
    // Validate input
    await _userManager.ValidateAsync(input);
    
    // Business logic
    var user = new User(GuidGenerator.Create(), input.Name, input.Email);
    await _userRepository.InsertAsync(user);
    
    return ObjectMapper.Map<User, UserDto>(user);
}
```

### SQL Injection Prevention

**Use parameterized queries**:

```csharp
// ✅ Good - parameterized query (EF Core)
var users = await _dbContext.Users
    .Where(u => u.Email == email)
    .ToListAsync();

// ✅ Good - parameterized raw SQL (if needed)
var users = await _dbContext.Users
    .FromSqlRaw("SELECT * FROM Users WHERE Email = {0}", email)
    .ToListAsync();

// ❌ Bad - string concatenation
var query = $"SELECT * FROM Users WHERE Email = '{email}'";
// Vulnerable to SQL injection!
```

### XSS (Cross-Site Scripting) Prevention

**Angular automatic escaping**:
```html
<!-- ✅ Good - Angular escapes by default -->
<div>{{ user.name }}</div>
<input [value]="user.email">

<!-- ⚠️ Dangerous - only use with trusted content -->
<div [innerHTML]="trustedHtml"></div>
```

**Sanitize user content**:
```typescript
import { DomSanitizer } from '@angular/platform-browser';

constructor(private sanitizer: DomSanitizer) {}

getSafeHtml(html: string) {
  return this.sanitizer.sanitize(SecurityContext.HTML, html);
}
```

### Authentication Patterns

**JWT Token Handling**:
```typescript
// ✅ Good - secure token storage
// Store in memory or httpOnly cookie
private token: string | null = null;

login(credentials: LoginDto): Observable<void> {
  return this.http.post<AuthResponse>('/api/auth/login', credentials)
    .pipe(
      tap(response => {
        this.token = response.accessToken;
        // Don't store in localStorage (XSS risk)
      })
    );
}

// Add token to requests
intercept(req: HttpRequest<any>, next: HttpHandler) {
  if (this.token) {
    req = req.clone({
      setHeaders: { Authorization: `Bearer ${this.token}` }
    });
  }
  return next.handle(req);
}
```

**Password Handling**:
```csharp
// ✅ Good - never log or store plain passwords
public async Task<bool> ValidatePasswordAsync(string email, string password)
{
    var user = await _userRepository.FindByEmailAsync(email);
    if (user == null) return false;
    
    // Use bcrypt or Identity password hasher
    return await _passwordHasher.VerifyHashedPasswordAsync(
        user, user.PasswordHash, password
    ) == PasswordVerificationResult.Success;
}

// ❌ Bad - logging sensitive data
Logger.LogInformation($"User {email} attempted login with password {password}");
```

### Data Encryption

**Encryption at Rest**:
- Database: AES-256 encryption enabled (Azure SQL)
- Files: Azure Storage with encryption
- Backups: Encrypted backups

**Encryption in Transit**:
```typescript
// ✅ Good - HTTPS only
// Enforced at infrastructure level
// TLS 1.3 required

// ❌ Bad - never use plain HTTP for sensitive data
```

**Sensitive Data Handling**:
```csharp
// ✅ Good - encrypt sensitive fields
public class User
{
    public string Email { get; set; }
    
    [DataProtection] // Custom attribute for field-level encryption
    public string SensitiveData { get; set; }
}
```

---

## Authentication & Authorization

### ABP.io Authorization

**Permission-based authorization**:
```csharp
// Define permissions
public static class KinanaPermissions
{
    public const string Users_View = "Kinana.Users.View";
    public const string Users_Edit = "Kinana.Users.Edit";
    public const string Users_Delete = "Kinana.Users.Delete";
}

// Protect endpoints
[Authorize(KinanaPermissions.Users_Edit)]
public async Task<UserDto> UpdateAsync(Guid id, UpdateUserDto input)
{
    // Only users with Users.Edit permission can access
}

// Check permissions in code
if (await AuthorizationService.IsGrantedAsync(KinanaPermissions.Users_Delete))
{
    // Allow delete operation
}
```

### Frontend Route Guards
```typescript
// ✅ Good - protect routes
@Injectable()
export class AuthGuard implements CanActivate {
  constructor(
    private authService: AuthService,
    private router: Router
  ) {}

  canActivate(): boolean {
    if (this.authService.isAuthenticated()) {
      return true;
    }
    
    this.router.navigate(['/login']);
    return false;
  }
}

// Apply to routes
{
  path: 'admin',
  canActivate: [AuthGuard],
  component: AdminComponent
}
```

---

## Dependency Security

### Regular Updates
```bash
# Check for vulnerabilities
npm audit
npm audit fix

# Backend
dotnet list package --vulnerable
```

### Automated Scanning
- GitHub Dependabot enabled
- Security alerts for vulnerable packages
- Regular dependency updates in sprint planning

---

## Secrets Management

### Never Commit Secrets
```bash
# ✅ Good - use environment variables
API_KEY=${API_KEY}
DATABASE_URL=${DATABASE_URL}

# ❌ Bad - hardcoded secrets
const API_KEY = 'abc123-secret-key';  // Never!
```

### Azure Key Vault
```csharp
// ✅ Good - retrieve from Key Vault
var apiKey = await _keyVaultService.GetSecretAsync("ApiKey");

// Store connection strings in Azure configuration
// Never in appsettings.json committed to git
```

### .gitignore
```
# Ensure secrets are ignored
.env
.env.local
*.key
*.pem
appsettings.Development.json
appsettings.Production.json
```

---

## API Security

### Rate Limiting
```csharp
// Apply rate limiting to prevent abuse
[HttpPost]
[RateLimit(MaxRequests = 100, TimeWindow = "1m")]
public async Task<IActionResult> SendEmail(EmailDto input)
{
    // Implementation
}
```

### CORS Configuration
```csharp
// ✅ Good - restrictive CORS
services.AddCors(options =>
{
    options.AddPolicy("KinanaPolicy", builder =>
    {
        builder
            .WithOrigins("https://kinana.com", "https://app.kinana.com")
            .AllowedMethods("GET", "POST", "PUT", "DELETE")
            .AllowCredentials();
    });
});

// ❌ Bad - allow all origins
builder.AllowAnyOrigin(); // Too permissive!
```

---

## Security Testing

### Code Review Checklist
- [ ] No hardcoded secrets or credentials
- [ ] Input validation present
- [ ] SQL injection prevented (parameterized queries)
- [ ] XSS prevention (output encoding)
- [ ] Authorization checks on protected operations
- [ ] Sensitive data encrypted
- [ ] Error messages don't leak information

### Dependency Scanning
```bash
# Run before each PR
npm audit
dotnet list package --vulnerable
```

### Manual Security Review
- Code review focuses on security implications
- Solution Architect reviews authentication/authorization
- External penetration testing (annual, planned)

---

## Incident Response

**If Security Issue Discovered**:
1. Notify Solution Architect immediately
2. Assess severity and impact
3. Implement fix ASAP (hotfix if in production)
4. Document incident and remediation
5. Review and update security practices

**Reference**: SharePoint D-IP-006 (Incident Response Plan)

---

## Security Training

**Required**:
- Annual security training for all developers
- OWASP Top 10 awareness
- Secure coding practices
- Incident reporting procedures

**Resources**:
- OWASP Top 10: https://owasp.org/www-project-top-10/
- OWASP Secure Coding Practices: https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/
- ABP Security: https://docs.abp.io/en/abp/latest/Authorization

---

## Resources

**External**:
- OWASP: https://owasp.org/
- NIST Cybersecurity Framework: https://www.nist.gov/cyberframework
- CIS Benchmarks: https://www.cisecurity.org/cis-benchmarks/

**Internal**:
- [Security Compliance](../compliance/Security_Compliance.md)
- SharePoint IP Governance (policies and procedures)
- Security audit reports

---

*Last Updated: November 2025*  
*Version: 1.0*  
*Note: Detailed security policies in Compliance & Governance documentation*
