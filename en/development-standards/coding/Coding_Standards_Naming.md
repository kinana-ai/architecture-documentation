# Naming Conventions

## Purpose

Consistent naming across the codebase improves readability and maintainability. These conventions apply across all languages (TypeScript, C#, Python) with language-specific casing rules.

---

## General Principles

### Descriptive Names
```typescript
// ✅ Good - clear purpose
function calculateTotalPrice(items: Item[]): number

// ❌ Bad - unclear
function calc(x: any[]): number
```

### Avoid Abbreviations (Unless Well-Known)
```csharp
// ✅ Good
public class UserRepository { }
public string EmailAddress { get; set; }

// ❌ Bad
public class UsrRepo { }  // What's "Usr"?
public string EmAddr { get; set; }

// ✅ OK - well-known abbreviations
public string Url { get; set; }
public int MaxCount { get; set; }
public string Id { get; set; }
```

### Pronounceable Names
```python
# ✅ Good
created_timestamp = datetime.now()

# ❌ Bad
crtd_ts = datetime.now()  # Hard to pronounce and discuss
```

---

## Language-Specific Casing

### TypeScript / JavaScript (Angular)
- **Files**: kebab-case (`user-profile.component.ts`)
- **Classes**: PascalCase (`UserProfileComponent`)
- **Functions/Methods**: camelCase (`getUserProfile()`)
- **Variables**: camelCase (`userName`)
- **Constants**: UPPER_CASE (`MAX_RETRY_ATTEMPTS`)
- **Interfaces**: PascalCase (`IUserService` or `UserService`)
- **Enums**: PascalCase for name, PascalCase for values (`UserRole.Admin`)

### C# (ABP.io)
- **Files**: PascalCase (`UserService.cs`)
- **Classes**: PascalCase (`UserService`)
- **Methods**: PascalCase (`GetUserProfile()`)
- **Properties**: PascalCase (`UserName`)
- **Private Fields**: camelCase with _ prefix (`_userRepository`)
- **Local Variables**: camelCase (`userName`)
- **Constants**: PascalCase (`MaxRetryAttempts`)
- **Interfaces**: PascalCase with I prefix (`IUserService`)

### Python
- **Files**: snake_case (`user_service.py`)
- **Classes**: PascalCase (`UserService`)
- **Functions**: snake_case (`get_user_profile()`)
- **Variables**: snake_case (`user_name`)
- **Constants**: UPPER_CASE (`MAX_RETRY_ATTEMPTS`)
- **"Private"**: _leading_underscore (`_internal_method()`)

---

## Component Names

### Frontend (Angular)

**Components**:
```typescript
// Pattern: [Feature][Type]Component
UserProfileComponent      // ✅ Good
UserListComponent
DocumentViewerComponent

// Files
user-profile.component.ts
user-list.component.ts
document-viewer.component.ts
```

**Services**:
```typescript
// Pattern: [Feature]Service
UserService              // ✅ Good
AuthenticationService
NotificationService

// Files
user.service.ts
authentication.service.ts
notification.service.ts
```

**Modules**:
```typescript
// Pattern: [Feature]Module
UserModule               // ✅ Good
LibraryModule
SharedModule

// Files
user.module.ts
library.module.ts
shared.module.ts
```

### Backend (ABP.io)

**Application Services**:
```csharp
// Pattern: [Entity]AppService
UserAppService           // ✅ Good
DocumentAppService
CourseAppService
```

**Domain Services**:
```csharp
// Pattern: [Domain]Manager or [Domain]DomainService
UserManager              // ✅ Good
SubscriptionManager
CourseEnrollmentDomainService
```

**Entities**:
```csharp
// Pattern: [Singular noun]
User                     // ✅ Good
Document
Course
Enrollment
```

**Repositories**:
```csharp
// Pattern: I[Entity]Repository
IUserRepository          // ✅ Good
IDocumentRepository
ICourseRepository
```

**DTOs**:
```csharp
// Pattern: [Action][Entity]Dto or [Entity]Dto
CreateUserDto            // ✅ Good - input
UpdateUserDto            // ✅ Good - input
UserDto                  // ✅ Good - output
UserListDto              // ✅ Good - list item
```

---

## Variable Names

### Boolean Variables
```typescript
// Prefix with is/has/can/should/will
const isActive = true;
const hasPermission = false;
const canEdit = user.role === 'admin';
const shouldRetry = attempts < maxAttempts;
const willExpire = expiryDate < currentDate;

// ❌ Bad - not clear it's boolean
const active = true;         // Could be string "active"
const permission = false;    // Ambiguous
```

### Collections
```typescript
// Plural names for arrays/lists
const users: User[] = [];
const documents: Document[] = [];

// Specific names for maps/dictionaries
const userById: Map<string, User> = new Map();
const documentCache: Record<string, Document> = {};

// ❌ Bad
const userList: User[] = [];  // Redundant "List"
const data: any[] = [];       // Too vague
```

### Counts and Indexes
```typescript
// Clear counting variables
const userCount = users.length;
const totalPages = Math.ceil(count / pageSize);
const activeUserCount = users.filter(u => u.isActive).length;

// Loop indexes
for (let i = 0; i < items.length; i++) { }      // ✅ i, j, k for simple loops
for (let userIndex = 0; ...) { }                // ✅ Descriptive for complex loops
```

### Temporary Variables
```typescript
// ✅ OK for short-lived variables in small scopes
const temp = a;
a = b;
b = temp;

// ✅ Better - descriptive even if temporary
const previousValue = currentValue;
currentValue = newValue;
```

---

## Function / Method Names

### Verb-Based Names
```typescript
// Actions should start with verbs
function getUser(id: string): User { }
function createDocument(data: CreateDocumentDto): Document { }
function updateProfile(userId: string, data: ProfileData): void { }
function deleteComment(commentId: string): void { }
function validateEmail(email: string): boolean { }
function calculateTotalPrice(items: Item[]): number { }

// ❌ Bad - not verb-based
function user(id: string): User { }              // What does this do?
function document(data: any): Document { }       // Create? Get? Update?
```

### Common Verb Prefixes
- **get**: Retrieve data (may throw if not found)
- **find**: Search for data (returns null if not found)
- **fetch**: Load data from external source
- **create**: Create new entity
- **update**: Modify existing entity
- **delete/remove**: Delete entity
- **save**: Persist entity (create or update)
- **validate**: Check if data is valid
- **calculate**: Perform computation
- **process**: Execute workflow
- **handle**: Event handler
- **on**: Event callback (`onClick`, `onSubmit`)

### Query Methods
```csharp
// Boolean queries
public bool IsActive() { }
public bool HasPermission(string permission) { }
public bool CanEdit() { }

// List queries  
public List<User> GetActiveUsers() { }
public List<Document> FindDocumentsByCategory(string category) { }
```

---

## Class and Interface Names

### Classes
```typescript
// Nouns or noun phrases
class UserProfile { }
class DocumentService { }
class AuthenticationManager { }
class HttpInterceptor { }

// ❌ Bad
class DoSomething { }  // Verb-based, should be function
class Data { }         // Too vague
```

### Interfaces (TypeScript)
```typescript
// No 'I' prefix (TypeScript convention)
interface User { }
interface UserService { }

// Or descriptive adjective
interface Serializable { }
interface Comparable { }
```

### Interfaces (C#)
```csharp
// 'I' prefix (C# convention)
public interface IUserService { }
public interface IRepository<T> { }
public interface ISerializable { }
```

### Abstract Classes
```csharp
// Optional 'Base' or 'Abstract' prefix
public abstract class BaseEntity { }
public abstract class AbstractValidator { }

// Or descriptive without prefix
public abstract class Entity { }
```

---

## Constants and Enums

### Constants
```typescript
// TypeScript / JavaScript
const MAX_RETRY_ATTEMPTS = 3;
const API_BASE_URL = 'https://api.kinana.com';
const DEFAULT_PAGE_SIZE = 20;

// C#
public const int MaxRetryAttempts = 3;
public const string ApiBaseUrl = "https://api.kinana.com";
private const int DefaultPageSize = 20;

// Python
MAX_RETRY_ATTEMPTS = 3
API_BASE_URL = 'https://api.kinana.com'
DEFAULT_PAGE_SIZE = 20
```

### Enums
```typescript
// TypeScript
enum UserRole {
  Student = 'student',
  Teacher = 'teacher',
  Admin = 'admin'
}

// C#
public enum UserRole
{
    Student,
    Teacher,
    Admin
}

// Python (using Enum class)
from enum import Enum

class UserRole(Enum):
    STUDENT = 'student'
    TEACHER = 'teacher'
    ADMIN = 'admin'
```

---

## Database / API Naming

### Database Tables
```sql
-- Plural, snake_case
users
documents
user_profiles
course_enrollments
```

### Database Columns
```sql
-- snake_case
id
user_name
email_address
created_at
is_active
```

### API Endpoints
```
-- RESTful, plural resources, kebab-case
GET    /api/users
POST   /api/users
GET    /api/users/:id
PUT    /api/users/:id
DELETE /api/users/:id

GET    /api/documents/:id/download
POST   /api/courses/:id/enroll
```

---

## File and Directory Names

### Frontend (Angular)
```
// kebab-case
components/
  user-profile/
    user-profile.component.ts
    user-profile.component.html
    user-profile.component.scss

services/
  user.service.ts
  authentication.service.ts

models/
  user.model.ts
  document.model.ts
```

### Backend (C#)
```
// PascalCase
Services/
  UserAppService.cs
  DocumentAppService.cs

Domain/
  Entities/
    User.cs
    Document.cs
  Repositories/
    IUserRepository.cs
```

### Python
```
# snake_case
models/
  user_model.py
  document_model.py

services/
  recommendation_service.py
  data_processor.py
```

---

## Acronyms and Initialisms

### Casing Rules
```typescript
// TypeScript / JavaScript (camelCase)
const userId = '123';              // ✅ Good
const xmlParser = new XmlParser(); // ✅ Good
const httpRequest = fetch(...);    // ✅ Good

// ❌ Bad
const userID = '123';
const XMLParser = new XMLParser();
const HTTPRequest = fetch(...);

// C# (PascalCase)
public string UserId { get; set; }       // ✅ Good
public class XmlParser { }               // ✅ Good
public HttpRequest CreateRequest() { }   // ✅ Good

// ❌ Bad
public string UserID { get; set; }
public class XMLParser { }

// Exception: 2-letter acronyms stay uppercase in C#
public string ID { get; set; }           // ✅ OK
public class IOHelper { }                // ✅ OK
```

---

## Special Cases

### Event Handlers
```typescript
// on[Event] or handle[Event]
function onClick(event: MouseEvent) { }
function onSubmit(form: FormData) { }
function handleUserLogin(credentials: LoginDto) { }
```

### React/Angular Callbacks
```typescript
// Props with on prefix
<button onClick={handleClick}>

// Angular outputs with EventEmitter
@Output() userSelected = new EventEmitter<User>();
```

### Async Methods
```csharp
// Async suffix in C#
public async Task<User> GetUserAsync(Guid id) { }
public async Task UpdateUserAsync(User user) { }
```

---

## Anti-Patterns to Avoid

```typescript
// ❌ Bad - single letter variables (except loops)
const u = getUser();      // Use 'user'
const d = new Date();     // Use 'date' or 'now'

// ❌ Bad - Hungarian notation
const strName = 'John';   // Just 'name'
const intCount = 5;       // Just 'count'
const bIsActive = true;   // Just 'isActive'

// ❌ Bad - redundant names
class UserClass { }                // Just 'User'
interface IUserInterface { }       // Just 'IUser' (C#) or 'User' (TS)
const userVariable = getUser();    // Just 'user'

// ❌ Bad - noise words
class UserInfo { }         // vs User or UserProfile
class DataManager { }      // vs appropriate specific name
function doStuff() { }     // Be specific!
```

---

## Resources

- **Clean Code** by Robert C. Martin (book)
- **TypeScript Style Guide**: https://google.github.io/styleguide/tsguide.html
- **C# Naming Guidelines**: https://learn.microsoft.com/en-us/dotnet/standard/design-guidelines/naming-guidelines
- **PEP 8 Naming**: https://peps.python.org/pep-0008/#naming-conventions

---

*Last Updated: November 2025*  
*Version: 1.0*
