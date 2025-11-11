# Code Documentation Standards

## When to Document

### Always Document

- Public APIs (methods, services exposed to other modules)
- Complex algorithms (non-obvious logic)
- Business rules (regulatory requirements, domain-specific logic)
- Workarounds (temporary fixes, known issues)
- Performance-critical code (optimizations that sacrifice readability)

### Rarely Document

- Simple getters/setters
- Obvious logic
- Well-named functions
- Self-explanatory code

### Never Document

- What the code does (code shows this)
- Outdated information
- Commented-out code (delete it, use git history)

---

## Documentation Requirements

### Frontend (TypeScript/Angular)

**Public Components**:

```typescript
/**
 * Displays user profile information with edit capabilities.
 *
 * Emits userUpdated event when profile is successfully saved.
 * Handles validation errors and displays appropriate messages.
 */
@Component({
  selector: "app-user-profile",
  templateUrl: "./user-profile.component.html",
})
export class UserProfileComponent {}
```

**Public Services**:

```typescript
/**
 * Manages user authentication and session state.
 *
 * Provides methods for login, logout, token refresh, and
 * permission checking. Automatically refreshes tokens before expiry.
 */
@Injectable({ providedIn: "root" })
export class AuthService {
  /**
   * Authenticates user with email and password.
   *
   * @param credentials User email and password
   * @returns Observable of authenticated user with token
   * @throws AuthenticationError if credentials invalid
   */
  login(credentials: LoginDto): Observable<AuthResponse> {}
}
```

**Complex Logic Only**:

```typescript
// ✅ Good - explains WHY
private calculateProRatedAmount(subscription: Subscription): number {
  // Pro-rate based on days remaining in billing cycle
  // per business requirement BR-123
  const daysInMonth = 30;
  const daysRemaining = this.getDaysUntilRenewal(subscription);
  return subscription.monthlyPrice * (daysRemaining / daysInMonth);
}
```

### Backend (C# / ABP.io)

**Application Services** (Public API):

```csharp
/// <summary>
/// User management application service.
/// Provides CRUD operations and business logic for users.
/// </summary>
public class UserAppService : ApplicationService, IUserAppService
{
    /// <summary>
    /// Retrieves user by unique identifier.
    /// </summary>
    /// <param name="id">User's unique identifier.</param>
    /// <returns>User details with role information.</returns>
    /// <exception cref="EntityNotFoundException">Thrown when user not found.</exception>
    [Authorize(KinanaPermissions.Users_View)]
    public async Task<UserDto> GetAsync(Guid id)
    {
        var user = await _userRepository.GetAsync(id);
        return ObjectMapper.Map<User, UserDto>(user);
    }
}
```

**Domain Entities**:

```csharp
/// <summary>
/// Represents a user in the Kinana platform.
/// Aggregate root containing user profile and authentication information.
/// </summary>
public class User : FullAuditedAggregateRoot<Guid>
{
    /// <summary>
    /// User's email address. Must be unique across the system.
    /// </summary>
    public string Email { get; private set; }

    /// <summary>
    /// Activates the user account.
    /// Sends welcome email and initializes default preferences.
    /// </summary>
    public void Activate()
    {
        // Business logic
    }
}
```

**Complex Logic**:

```csharp
private async Task<bool> ValidateSubscriptionEligibility(User user)
{
    // Business rule: Users must have active email verification
    // and no pending payment issues to upgrade subscription
    // See business requirements doc BR-456

    if (!user.EmailConfirmed)
        return false;

    var hasPendingPayments = await _paymentService.HasPendingPaymentsAsync(user.Id);
    return !hasPendingPayments;
}
```

### Python (AI Development)

**Module Docstrings**:

```python
"""
Content recommendation model for Kinana platform.

This module implements collaborative filtering algorithm for suggesting
educational content to students based on their learning history and
peer behavior patterns.

Requires:
    - pandas >= 2.0
    - torch >= 2.0
    - scikit-learn >= 1.3

Example:
    model = ContentRecommender(embedding_dim=128)
    recommendations = model.predict(user_id, top_k=10)
"""
```

**Function Docstrings**:

```python
def train_model(data: pd.DataFrame, epochs: int = 10, learning_rate: float = 0.001) -> Model:
    """
    Train content recommendation model on user interaction data.

    Args:
        data: Training data with columns [user_id, content_id, interaction_type, timestamp]
        epochs: Number of training epochs (default: 10)
        learning_rate: Learning rate for optimizer (default: 0.001)

    Returns:
        Trained model ready for inference

    Raises:
        ValueError: If data is empty or missing required columns
        RuntimeError: If GPU not available and CUDA required

    Example:
        >>> data = load_training_data('data/interactions.csv')
        >>> model = train_model(data, epochs=20)
        >>> model.save('models/recommender_v1.pt')
    """
    pass
```

**Complex Algorithms**:

```python
def compute_similarity_matrix(embeddings: np.ndarray) -> np.ndarray:
    """
    Compute cosine similarity between all content embeddings.

    Uses optimized matrix multiplication instead of pairwise computation
    for performance. Memory complexity: O(n²) where n is number of items.
    """
    # Normalize embeddings to unit vectors
    norms = np.linalg.norm(embeddings, axis=1, keepdims=True)
    normalized = embeddings / norms

    # Cosine similarity via dot product of normalized vectors
    return np.dot(normalized, normalized.T)
```

---

## Commenting Standards

### Inline Comments

**Good Comments**:

```typescript
// Exponential backoff to avoid overwhelming API during high load
await sleep(2 ** retryCount * 1000);

// VAT exempt for educational institutions per UAE tax law
if (organization.type === "educational") {
  applyVat = false;
}

// HACK: Temporary workaround for Safari PDF rendering bug (Issue #456)
// Remove after Safari 17.2 update
if (isSafari && version < 17.2) {
  useFallbackRenderer = true;
}
```

**Bad Comments**:

```typescript
// ❌ States the obvious
// Loop through users
users.forEach((user) => processUser(user));

// ❌ What, not why
// Set flag to true
isProcessed = true;

// ❌ Outdated
// TODO: Fix this bug (already fixed 6 months ago)
```

### TODO Comments

**Format**:

```typescript
// TODO: Refactor to use async/await (Issue #789)
// TODO(username): Add caching for performance
// FIXME: Race condition in concurrent updates (Critical - Issue #456)
// HACK: Workaround for third-party library bug, remove in v2.0
```

**Track in GitHub**: Convert important TODOs to GitHub Issues

---

## Documentation Tools

### TypeScript/JavaScript (JSDoc)

**Installation**:

```bash
npm install --save-dev jsdoc
```

**Configuration** (.jsdoc.json):

```json
{
  "source": {
    "include": ["src"],
    "includePattern": ".+\\.ts$"
  },
  "opts": {
    "destination": "./docs",
    "recurse": true
  }
}
```

**Usage**:

```typescript
/**
 * @typedef {Object} UserProfile
 * @property {string} id - User unique identifier
 * @property {string} name - User display name
 * @property {string[]} roles - User role names
 */

/**
 * Fetches user profile from API
 * @param {string} userId - The user ID to fetch
 * @returns {Promise<UserProfile>} User profile object
 * @throws {NotFoundError} When user doesn't exist
 */
async function getUserProfile(userId: string): Promise<UserProfile> {}
```

### C# (XML Documentation)

**Enable in Project**:

```xml
<PropertyGroup>
  <GenerateDocumentationFile>true</GenerateDocumentationFile>
  <NoWarn>1591</NoWarn> <!-- Disable warning for missing XML comments -->
</PropertyGroup>
```

**XML Tags**:

```csharp
/// <summary>Brief description</summary>
/// <remarks>Additional details</remarks>
/// <param name="paramName">Parameter description</param>
/// <returns>Return value description</returns>
/// <exception cref="ExceptionType">When this exception is thrown</exception>
/// <example>Usage example with code</example>
/// <see cref="RelatedClass"/>
```

**Generate Documentation**:

- DocFX: https://dotnet.github.io/docfx/
- Sandcastle: https://github.com/EWSoftware/SHFB

### Python (Docstrings)

**Style**: Google or NumPy format

**Google Style**:

```python
def function_name(param1: str, param2: int) -> bool:
    """Brief description of function.

    Longer description if needed. Can span multiple lines
    and include additional context.

    Args:
        param1: Description of param1
        param2: Description of param2

    Returns:
        Description of return value

    Raises:
        ValueError: When param1 is empty
        RuntimeError: When operation fails

    Example:
        >>> result = function_name("test", 42)
        >>> print(result)
        True
    """
    pass
```

**NumPy Style**:

```python
def function_name(param1, param2):
    """
    Brief description of function.

    Longer description if needed.

    Parameters
    ----------
    param1 : str
        Description of param1
    param2 : int
        Description of param2

    Returns
    -------
    bool
        Description of return value

    Raises
    ------
    ValueError
        When param1 is empty

    Examples
    --------
    >>> result = function_name("test", 42)
    True
    """
    pass
```

**Generate Documentation**:

```bash
# Sphinx
pip install sphinx
sphinx-quickstart
sphinx-apidoc -o docs/source .
make html

# pdoc
pip install pdoc3
pdoc --html --output-dir docs module_name
```

---

## API Documentation

### REST API Documentation

**OpenAPI/Swagger** (ABP.io built-in):

- Auto-generated from controllers
- Available at `/swagger`
- XML comments populate descriptions

**Enhance with Examples**:

```csharp
/// <summary>
/// Creates a new user
/// </summary>
/// <remarks>
/// Sample request:
///
///     POST /api/users
///     {
///        "name": "John Doe",
///        "email": "john@example.com"
///     }
///
/// </remarks>
[HttpPost]
public async Task<UserDto> CreateAsync(CreateUserDto input) { }
```

## README Standards

**See**: [File Header Standards - README](./file-headers/File_Header_Standards.md)

---

## Best Practices

### Keep It Short

- One-line summary preferred
- Details only when necessary
- Link to external docs for lengthy explanations

### Keep It Current

- Update docs when code changes
- Remove outdated comments
- Regular doc review during refactoring

### Use Tools

- Leverage IDE support (IntelliSense, autocomplete)
- Generate docs from code when possible
- Validate docs in CI/CD (planned)

### Document Decisions

- Architecture Decision Records (ADRs) for major choices
- Comments for non-obvious implementations
- Link to GitHub Issues for context

---

## Resources

**TypeScript/JavaScript**:

- JSDoc: https://jsdoc.app/
- TSDoc: https://tsdoc.org/

**C#**:

- XML Documentation: https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/xmldoc/
- DocFX: https://dotnet.github.io/docfx/

**Python**:

- PEP 257: https://peps.python.org/pep-0257/
- Google Python Style Guide: https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings
- Sphinx: https://www.sphinx-doc.org/

---

_Last Updated: November 2025_  
_Version: 1.0_
