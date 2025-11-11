# Best Practices

## Overview

Universal best practices applicable across all languages and contexts. These principles ensure maintainable, secure, and performant code.

**Philosophy**: "Any fool can write code that a computer can understand. Good programmers write code that humans can understand." - Martin Fowler

---

## Code Readability

### Write Self-Documenting Code

**Descriptive Names**:
```typescript
// ✅ Good
function calculateMonthlySubscriptionRevenue(users: User[]): number

// ❌ Bad
function calc(u: any[]): number
```

**Small, Focused Functions**:
```csharp
// ✅ Good - single responsibility
public bool IsEligibleForDiscount(User user)
{
    return user.IsActive && user.SubscriptionYears >= 1;
}

// ❌ Bad - too much in one function
public decimal ProcessUserPayment(User user, decimal amount)
{
    // Check eligibility
    // Calculate discount
    // Process payment
    // Send email
    // Update database
    // Log transaction
    // ... 200 lines of code
}
```

**Extract Magic Numbers**:
```python
# ✅ Good
MAX_LOGIN_ATTEMPTS = 3
SESSION_TIMEOUT_MINUTES = 30

if attempts > MAX_LOGIN_ATTEMPTS:
    lock_account(user)

# ❌ Bad
if attempts > 3:  # What is 3?
    lock_account(user)
```

---

## Error Handling

### Always Handle Errors Gracefully

**Catch Specific Exceptions**:
```typescript
// ✅ Good
try {
  const data = await loadUserData(userId);
} catch (error) {
  if (error instanceof NetworkError) {
    showRetryDialog();
  } else if (error instanceof NotFoundError) {
    redirectToNotFound();
  } else {
    logError(error);
    showGenericError();
  }
}

// ❌ Bad - swallowing errors
try {
  await loadUserData(userId);
} catch (error) {
  // Do nothing
}
```

**Fail Fast**:
```csharp
// ✅ Good - validate early
public void ProcessOrder(Order order)
{
    if (order == null)
        throw new ArgumentNullException(nameof(order));
    
    if (order.Items.Count == 0)
        throw new BusinessException("Order must have at least one item");
    
    // Process order
}

// ❌ Bad - check late
public void ProcessOrder(Order order)
{
    // 100 lines of processing
    if (order == null) // Too late!
        return;
}
```

**Provide Context in Exceptions**:
```python
# ✅ Good - informative error messages
if balance < amount:
    raise InsufficientFundsError(
        f"Insufficient funds: balance={balance}, required={amount}"
    )

# ❌ Bad - vague errors
if balance < amount:
    raise Exception("Error")
```

---

## Security

### Input Validation

**Never Trust User Input**:
```typescript
// ✅ Good - validate everything
function createUser(input: CreateUserDto): User {
  if (!input.email || !isValidEmail(input.email)) {
    throw new ValidationError('Invalid email');
  }
  
  if (!input.password || input.password.length < 12) {
    throw new ValidationError('Password must be at least 12 characters');
  }
  
  // Sanitize input
  const sanitizedName = sanitizeInput(input.name);
  
  return new User(input.email, sanitizedName, hashPassword(input.password));
}

// ❌ Bad - no validation
function createUser(input: any): User {
  return new User(input.email, input.name, input.password);
}
```

### Output Encoding

**Prevent XSS**:
```typescript
// ✅ Good - use framework's built-in escaping
// Angular auto-escapes
<div>{{ user.bio }}</div>

// For trusted HTML, explicitly sanitize
<div [innerHTML]="sanitizer.sanitize(SecurityContext.HTML, user.bio)"></div>

// ❌ Bad - direct HTML injection
<div [innerHTML]="user.bio"></div>  // Dangerous!
```

### Secure Authentication

**No Plain Text Passwords**:
```csharp
// ✅ Good - hash passwords
var hashedPassword = _passwordHasher.HashPassword(user, password);
user.PasswordHash = hashedPassword;

// ❌ Bad - storing plain text
user.Password = password;  // Never!
```

**Secure Session Management**:
```typescript
// ✅ Good - httpOnly cookies or in-memory token storage
// ❌ Bad - localStorage for sensitive tokens (XSS vulnerable)
localStorage.setItem('authToken', token);  // Avoid!
```

---

## Performance

### Don't Premature Optimize

**Write Clean Code First**:
```python
# ✅ Good - readable first
def calculate_total(items):
    return sum(item.price * item.quantity for item in items)

# ❌ Bad - premature micro-optimization
def calculate_total(items):
    # Complex bit manipulation to save 2 nanoseconds
    pass
```

**Optimize When Needed**:
- Measure before optimizing (profiling tools)
- Focus on algorithmic improvements (O(n²) → O(n))
- Optimize hot paths, not cold paths

### Avoid N+1 Queries

**Database Efficiency**:
```csharp
// ✅ Good - eager loading
var users = await _context.Users
    .Include(u => u.Profile)
    .Include(u => u.Roles)
    .ToListAsync();

// ❌ Bad - N+1 queries
var users = await _context.Users.ToListAsync();
foreach (var user in users)
{
    var profile = await _context.Profiles
        .FirstAsync(p => p.UserId == user.Id);  // N+1!
}
```

### Cache Appropriately

**Cache Expensive Operations**:
```typescript
// ✅ Good - cache static data
private categoryCache: Category[] | null = null;

async getCategories(): Promise<Category[]> {
  if (this.categoryCache) {
    return this.categoryCache;
  }
  
  this.categoryCache = await this.http.get<Category[]>('/api/categories').toPromise();
  return this.categoryCache;
}

// ⚠️ Be careful - invalidate cache when data changes
```

---

## Maintainability

### DRY (Don't Repeat Yourself)

**Extract Reusable Code**:
```python
# ✅ Good - reusable function
def format_currency(amount, currency='USD'):
    return f"{currency} {amount:.2f}"

order_total = format_currency(order.total)
tax_amount = format_currency(order.tax)

# ❌ Bad - repetition
order_total = f"USD {order.total:.2f}"
tax_amount = f"USD {order.tax:.2f}"
```

### Single Responsibility Principle

**One Reason to Change**:
```csharp
// ✅ Good - focused classes
public class UserValidator
{
    public void Validate(User user) { }
}

public class UserRepository
{
    public async Task<User> GetAsync(Guid id) { }
}

public class UserEmailService
{
    public async Task SendWelcomeEmailAsync(User user) { }
}

// ❌ Bad - god class
public class UserManager
{
    public void Validate(User user) { }
    public async Task<User> GetAsync(Guid id) { }
    public async Task SendEmailAsync(User user) { }
    public void GenerateReport() { }
    // ... 50 more methods
}
```

### YAGNI (You Aren't Gonna Need It)

**Don't Over-Engineer**:
```typescript
// ✅ Good - simple solution for current needs
function getUserName(user: User): string {
  return user.name;
}

// ❌ Bad - over-engineered for hypothetical futures
interface UserNameStrategy {
  format(user: User): string;
}

class FormalNameStrategy implements UserNameStrategy { }
class CasualNameStrategy implements UserNameStrategy { }
class InternationalNameStrategy implements UserNameStrategy { }

// Using complex pattern for simple task
```

---

## Code Organization

### Logical Grouping

**Organize Imports**:
```typescript
// ✅ Good - grouped imports
// Angular
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

// Third-party
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

// App
import { UserService } from './user.service';
import { User } from './user.model';
```

**Consistent File Structure**:
```
// Components organized by feature
components/
  user/
    user-list/
    user-detail/
    user-edit/
  library/
    document-list/
    document-viewer/
```

### Component Size

**Keep Components Small**:
- Single file < 400 lines
- Extract complex logic to services
- Break large components into smaller ones
- One component per file

---

## Testing (Future)

### Write Testable Code

**Dependency Injection**:
```csharp
// ✅ Good - testable
public class UserService
{
    private readonly IUserRepository _repository;
    
    public UserService(IUserRepository repository)
    {
        _repository = repository;
    }
    
    public async Task<User> GetUserAsync(Guid id)
    {
        return await _repository.GetAsync(id);
    }
}

// Easy to test by mocking IUserRepository
```

**Pure Functions**:
```python
# ✅ Good - pure function (testable)
def calculate_discount(price: float, discount_percent: float) -> float:
    return price * (1 - discount_percent / 100)

# No side effects, same input = same output
```

---

## Comments

### When to Comment

**Explain WHY, Not WHAT**:
```typescript
// ✅ Good - explains reasoning
// Use exponential backoff to avoid overwhelming the API
// during high traffic periods
await sleep(2 ** retryCount * 1000);

// ✅ Good - explains business rule
// Per regulatory requirement ABC-123, we must retain
// user data for 7 years
const RETENTION_YEARS = 7;

// ❌ Bad - states the obvious
// Increment counter
counter++;

// ❌ Bad - what the code already shows
// Loop through users
users.forEach(user => {
  // Process user
  processUser(user);
});
```

### TODO Comments

**Track Technical Debt**:
```csharp
// TODO: Refactor this to use async/await (Issue #456)
// TODO: Add caching to improve performance
// TODO: Extract this into separate service
// HACK: Temporary workaround for issue #789, remove after v1.1
```

---

## Git Practices

### Atomic Commits

**One Logical Change Per Commit**:
```bash
# ✅ Good
git commit -m "feat(auth): add JWT token validation"
git commit -m "feat(auth): implement refresh token"
git commit -m "test(auth): add token validation tests"

# ❌ Bad - multiple unrelated changes
git commit -m "add auth, fix bug, update readme"
```

### Clear Commit Messages

**Follow Conventional Commits**:
```bash
# ✅ Good - clear and descriptive
git commit -m "fix(library): resolve PDF rendering issue on Safari

PDFs were not rendering correctly on Safari due to
CORS issue with Azure Blob Storage. Added proper
CORS headers to fix.

Fixes #234"

# ❌ Bad - vague
git commit -m "fix bug"
```

---

## Code Review

### Be Constructive

**Helpful Feedback**:
```markdown
# ✅ Good
This could cause a memory leak because the subscription 
isn't unsubscribed. Consider using the takeUntil pattern
with a destroy$ subject.

# ✅ Good
Why did you choose this approach? The built-in method
might be more efficient and easier to maintain.

# ❌ Bad
This is wrong.

# ❌ Bad
Rewrite this.
```

### Accept Feedback Gracefully

- Don't take it personally
- Ask questions to understand
- Explain your reasoning if needed
- Update code based on valid feedback

---

## Resources

### Books
- **Clean Code** by Robert C. Martin
- **The Pragmatic Programmer** by Hunt & Thomas
- **Refactoring** by Martin Fowler

### Online
- **SOLID Principles**: https://en.wikipedia.org/wiki/SOLID
- **Code Smells**: https://refactoring.guru/refactoring/smells
- **Design Patterns**: https://refactoring.guru/design-patterns

---

*Last Updated: November 2025*  
*Version: 1.0*
