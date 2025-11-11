# C# / .NET Style Guide

## Primary References

**Official Standards**:
- [C# Coding Conventions](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/coding-style/coding-conventions) (Microsoft)
- [ABP Best Practices](https://docs.abp.io/en/abp/latest/Best-Practices/Index) (Framework-specific)

This document highlights Kinana-specific conventions and ABP.io patterns for senior developers.

---

## File Organization

### ABP.io Project Structure (DDD Layers)
```
Kinana.Domain/              # Domain entities, value objects, domain services
Kinana.Domain.Shared/       # Shared constants, enums
Kinana.Application/         # Application services, DTOs
Kinana.Application.Contracts/ # Service interfaces, DTOs
Kinana.EntityFrameworkCore/ # EF Core DbContext, repositories
Kinana.HttpApi/             # API controllers
Kinana.HttpApi.Client/      # HTTP client proxies
Kinana.Web/                 # UI (if applicable)
```

### File Naming
- **PascalCase** for all file names: `UserService.cs`
- **One class per file**: `User.cs` contains `User` class
- **Match class name**: File `UserAppService.cs` contains `UserAppService`

---

## Naming Conventions

### Casing Rules
```csharp
// PascalCase for classes, methods, properties, namespaces
public class UserService { }
public void GetUser() { }
public string UserName { get; set; }

// camelCase for private fields (with _ prefix)
private readonly IUserRepository _userRepository;
private string _userName;

// camelCase for local variables and parameters
public void ProcessUser(string userId)
{
    var userName = GetUserName(userId);
}

// PascalCase for constants
public const int MaxRetryAttempts = 3;
private const string ApiBaseUrl = "https://api.kinana.com";
```

### Interfaces
```csharp
// Prefix with 'I'
public interface IUserService { }
public interface IRepository<T> { }
```

### Async Methods
```csharp
// Suffix with 'Async'
public async Task<User> GetUserAsync(Guid id) { }
public async Task UpdateUserAsync(User user) { }
```

### Boolean Properties/Methods
```csharp
// Use Is/Has/Can/Should prefix
public bool IsActive { get; set; }
public bool HasPermission(string permission) { }
public bool CanEdit() { }
```

---

## ABP.io Patterns

### Application Services
```csharp
// Inherit from ApplicationService, implement interface
public class UserAppService : ApplicationService, IUserAppService
{
    private readonly IUserRepository _userRepository;
    
    public UserAppService(IUserRepository userRepository)
    {
        _userRepository = userRepository;
    }
    
    // Public API methods
    [Authorize(KinanaPermissions.Users_View)]
    public async Task<UserDto> GetAsync(Guid id)
    {
        var user = await _userRepository.GetAsync(id);
        return ObjectMapper.Map<User, UserDto>(user);
    }
    
    [Authorize(KinanaPermissions.Users_Edit)]
    public async Task<UserDto> UpdateAsync(Guid id, UpdateUserDto input)
    {
        var user = await _userRepository.GetAsync(id);
        
        // Update entity
        user.SetName(input.Name);
        user.SetEmail(input.Email);
        
        await _userRepository.UpdateAsync(user);
        
        return ObjectMapper.Map<User, UserDto>(user);
    }
}
```

### Domain Entities
```csharp
// Aggregate root with business logic
public class User : FullAuditedAggregateRoot<Guid>
{
    public string Name { get; private set; }
    public string Email { get; private set; }
    public bool IsActive { get; private set; }
    
    // Private constructor for EF Core
    private User() { }
    
    // Factory method for creation
    public User(Guid id, string name, string email)
        : base(id)
    {
        SetName(name);
        SetEmail(email);
        IsActive = true;
    }
    
    // Business logic methods with validation
    public void SetName(string name)
    {
        Name = Check.NotNullOrWhiteSpace(name, nameof(name));
    }
    
    public void SetEmail(string email)
    {
        // Validation logic
        if (!email.Contains("@"))
            throw new BusinessException("Invalid email format");
            
        Email = email;
    }
    
    public void Deactivate()
    {
        IsActive = false;
    }
}
```

### DTOs (Data Transfer Objects)
```csharp
// Input DTO
public class CreateUserDto
{
    [Required]
    [StringLength(128)]
    public string Name { get; set; }
    
    [Required]
    [EmailAddress]
    public string Email { get; set; }
}

// Output DTO
public class UserDto : EntityDto<Guid>
{
    public string Name { get; set; }
    public string Email { get; set; }
    public bool IsActive { get; set; }
}
```

### Repositories
```csharp
// Repository interface (if custom queries needed)
public interface IUserRepository : IRepository<User, Guid>
{
    Task<List<User>> GetActiveUsersAsync();
}

// Repository implementation
public class EfCoreUserRepository : EfCoreRepository<KinanaDbContext, User, Guid>, IUserRepository
{
    public EfCoreUserRepository(IDbContextProvider<KinanaDbContext> dbContextProvider)
        : base(dbContextProvider)
    {
    }
    
    public async Task<List<User>> GetActiveUsersAsync()
    {
        return await (await GetDbSetAsync())
            .Where(u => u.IsActive)
            .ToListAsync();
    }
}
```

---

## C# Language Features

### Async/Await
```csharp
// ✅ Good - async all the way
public async Task<User> GetUserAsync(Guid id)
{
    var user = await _userRepository.GetAsync(id);
    var profile = await _profileService.GetProfileAsync(user.Id);
    return user;
}

// ❌ Bad - blocking async code
public User GetUser(Guid id)
{
    return _userRepository.GetAsync(id).Result; // Don't block async!
}
```

### Null Handling (C# 12)
```csharp
// ✅ Good - null-conditional and null-coalescing
var userName = user?.Name ?? "Unknown";

// ✅ Good - null-forgiving when you're certain
var user = await _userRepository.FindAsync(id);
return user!; // We checked, it's not null

// ✅ Good - pattern matching
if (user is not null)
{
    // Use user
}
```

### Using Statements
```csharp
// ✅ Good - simplified using
using var stream = File.OpenRead("data.txt");
// Auto-disposed at end of scope

// ✅ Good - implicit using for file-scoped
using System;
using System.Collections.Generic;
using System.Threading.Tasks;
// No need for namespace wrapping
```

### Record Types (for immutable DTOs)
```csharp
// ✅ Good for read-only DTOs
public record UserSummaryDto(Guid Id, string Name, string Email);

// Usage
var summary = new UserSummaryDto(userId, "John", "john@example.com");
```

---

## LINQ Best Practices

### Prefer LINQ Query Syntax for Readability
```csharp
// ✅ Good - readable LINQ
var activeUsers = await (await GetDbSetAsync())
    .Where(u => u.IsActive)
    .OrderBy(u => u.Name)
    .ToListAsync();

// ✅ Good - async LINQ with EF Core
var userCount = await (await GetDbSetAsync())
    .CountAsync(u => u.IsActive);
```

### Avoid N+1 Query Problem
```csharp
// ✅ Good - eager loading
var users = await (await GetDbSetAsync())
    .Include(u => u.Profile)
    .Include(u => u.Roles)
    .ToListAsync();

// ❌ Bad - causes N+1 queries
var users = await (await GetDbSetAsync()).ToListAsync();
foreach (var user in users)
{
    var profile = await _profileRepository.GetAsync(user.ProfileId); // N+1!
}
```

---

## Exception Handling

### Use Specific Exceptions
```csharp
// ✅ Good - specific exception types
public async Task UpdateUserAsync(Guid id, UpdateUserDto input)
{
    var user = await _userRepository.FindAsync(id);
    
    if (user == null)
        throw new EntityNotFoundException(typeof(User), id);
    
    if (!await HasPermissionAsync(user))
        throw new AbpAuthorizationException();
    
    // Update logic
}

// ✅ Good - business exception
if (user.Email == input.NewEmail)
    throw new BusinessException("New email must be different");
```

### Try-Catch Appropriately
```csharp
// ✅ Good - catch specific exceptions you can handle
try
{
    await _externalApiService.SendDataAsync(data);
}
catch (HttpRequestException ex)
{
    Logger.LogWarning(ex, "External API unavailable, will retry later");
    await _queue.EnqueueAsync(data);
}

// ❌ Bad - swallowing all exceptions
try
{
    await SomeOperation();
}
catch { } // Don't do this!
```

---

## Dependency Injection

### Constructor Injection
```csharp
// ✅ Good - constructor injection
public class UserAppService : ApplicationService
{
    private readonly IUserRepository _userRepository;
    private readonly IEmailSender _emailSender;
    private readonly ILogger<UserAppService> _logger;
    
    public UserAppService(
        IUserRepository userRepository,
        IEmailSender emailSender,
        ILogger<UserAppService> logger)
    {
        _userRepository = userRepository;
        _emailSender = emailSender;
        _logger = logger;
    }
}

// ❌ Bad - service locator pattern
public class UserAppService
{
    public void DoSomething()
    {
        var service = ServiceProvider.GetService<IUserService>(); // Avoid!
    }
}
```

---

## Comments and Documentation

### XML Documentation for Public API
```csharp
/// <summary>
/// Retrieves a user by their unique identifier.
/// </summary>
/// <param name="id">The user's unique identifier.</param>
/// <returns>The user entity.</returns>
/// <exception cref="EntityNotFoundException">Thrown when user not found.</exception>
public async Task<UserDto> GetAsync(Guid id)
{
    var user = await _userRepository.GetAsync(id);
    return ObjectMapper.Map<User, UserDto>(user);
}
```

### Inline Comments Sparingly
```csharp
// ✅ Good - explains WHY
// We must wait 1 second between API calls per vendor rate limit
await Task.Delay(1000);

// ❌ Bad - states the obvious
// Get user by ID
var user = await _userRepository.GetAsync(id);
```

---

## Performance Considerations

### Use ValueTask for Hot Paths
```csharp
// When method may complete synchronously
public ValueTask<User> GetCachedUserAsync(Guid id)
{
    if (_cache.TryGetValue(id, out var user))
        return new ValueTask<User>(user); // Synchronous path
    
    return new ValueTask<User>(LoadUserAsync(id)); // Async path
}
```

### Avoid Boxing
```csharp
// ✅ Good - generic constraint
public void LogValue<T>(T value) where T : struct
{
    Logger.LogInformation("Value: {Value}", value);
}

// ❌ Bad - boxing value types
public void LogValue(object value)
{
    Logger.LogInformation("Value: {Value}", value); // Boxing!
}
```

### Use Span<T> for Performance-Critical Code
```csharp
// For memory-efficient operations
public void ProcessData(ReadOnlySpan<byte> data)
{
    // Process data without allocation
}
```

---

## Code Formatting

### EditorConfig
```ini
# .editorconfig
root = true

[*.cs]
indent_style = space
indent_size = 4
end_of_line = crlf

# Microsoft .NET conventions
dotnet_sort_system_directives_first = true
csharp_prefer_braces = true
csharp_new_line_before_open_brace = all
```

### Automatic Formatting
- Use built-in Visual Studio / VS Code formatter
- Format on save enabled
- Consistent team-wide formatting

---

## Testing (Future)

### Testable Code Structure
```csharp
// ✅ Good - testable through dependency injection
public class UserAppService : ApplicationService
{
    private readonly IUserRepository _userRepository;
    
    public UserAppService(IUserRepository userRepository)
    {
        _userRepository = userRepository;
    }
    
    public async Task<bool> IsUserActiveAsync(Guid id)
    {
        var user = await _userRepository.GetAsync(id);
        return user.IsActive;
    }
}

// Easy to test by mocking IUserRepository
```

---

## Resources

- **C# Coding Conventions**: https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/coding-style/coding-conventions
- **ABP Documentation**: https://docs.abp.io/
- **ABP Best Practices**: https://docs.abp.io/en/abp/latest/Best-Practices/Index
- **.NET Design Guidelines**: https://learn.microsoft.com/en-us/dotnet/standard/design-guidelines/
- **Async/Await Best Practices**: https://learn.microsoft.com/en-us/archive/msdn-magazine/2013/march/async-await-best-practices-in-asynchronous-programming

---

*Last Updated: November 2025*  
*Version: 1.0*
