# JavaScript / TypeScript Style Guide

## Primary Reference

**Official**: [Angular Style Guide](https://angular.io/guide/styleguide)

This document highlights Kinana-specific conventions and most important standards for senior developers. For comprehensive coverage, reference the Angular Style Guide.

---

## File Organization

### Angular Component Structure
```
component-name/
├── component-name.component.ts       # Component logic
├── component-name.component.html     # Template
├── component-name.component.scss     # Styles
├── component-name.component.spec.ts  # Tests (future)
└── index.ts                          # Barrel export (optional)
```

### File Naming
- **Components**: `feature-name.component.ts`
- **Services**: `feature-name.service.ts`
- **Models**: `feature-name.model.ts`
- **Interfaces**: `feature-name.interface.ts` or inline in component/service
- **Modules**: `feature-name.module.ts`

### One Class Per File
```typescript
// ✅ Good
// user.service.ts
export class UserService { }

// ❌ Bad - multiple classes in one file
export class UserService { }
export class UserRepository { }
```

---

## TypeScript Conventions

### Use Strict Mode
```json
// tsconfig.json
{
  "compilerOptions": {
    "strict": true,
    "noImplicitAny": true,
    "strictNullChecks": true
  }
}
```

### Type Annotations
```typescript
// ✅ Good - explicit types for public API
function getUser(id: string): Observable<User> {
  return this.http.get<User>(`/api/users/${id}`);
}

// ✅ Good - type inference for internal variables
const userName = user.name; // TypeScript infers string

// ❌ Bad - any type
function processData(data: any) { } // Avoid any
```

### Interfaces Over Classes for Data
```typescript
// ✅ Good - interface for data model
export interface User {
  id: string;
  name: string;
  email: string;
}

// ❌ Bad - class for simple data
export class User {
  id: string;
  name: string;
  email: string;
}
```

---

## Naming Conventions

### Files and Components
- **kebab-case** for file names: `user-profile.component.ts`
- **PascalCase** for class names: `UserProfileComponent`

### Variables and Functions
```typescript
// camelCase for variables and functions
const userName = 'John';
function getUserProfile() { }

// PascalCase for classes, interfaces, types
class UserService { }
interface UserProfile { }
type UserId = string;

// UPPER_CASE for constants
const MAX_RETRY_ATTEMPTS = 3;
const API_BASE_URL = 'https://api.kinana.com';
```

### Booleans
```typescript
// Prefix with is/has/can/should
const isActive = true;
const hasPermission = false;
const canEdit = user.role === 'admin';
const shouldShowWarning = errors.length > 0;
```

---

## Angular Patterns

### Component Structure
```typescript
@Component({
  selector: 'app-user-profile',
  templateUrl: './user-profile.component.html',
  styleUrls: ['./user-profile.component.scss']
})
export class UserProfileComponent implements OnInit, OnDestroy {
  // 1. Public properties (template binding)
  user: User | null = null;
  isLoading = false;
  
  // 2. Private properties
  private destroy$ = new Subject<void>();
  
  // 3. Constructor (dependency injection)
  constructor(
    private userService: UserService,
    private router: Router
  ) {}
  
  // 4. Lifecycle hooks
  ngOnInit(): void {
    this.loadUser();
  }
  
  ngOnDestroy(): void {
    this.destroy$.next();
    this.destroy$.complete();
  }
  
  // 5. Public methods (template binding)
  onSave(): void {
    // ...
  }
  
  // 6. Private methods
  private loadUser(): void {
    this.userService.getUser()
      .pipe(takeUntil(this.destroy$))
      .subscribe(user => this.user = user);
  }
}
```

### Service Structure
```typescript
@Injectable({
  providedIn: 'root' // Singleton service
})
export class UserService {
  private readonly apiUrl = '/api/users';
  
  constructor(private http: HttpClient) {}
  
  getUser(id: string): Observable<User> {
    return this.http.get<User>(`${this.apiUrl}/${id}`);
  }
  
  updateUser(id: string, user: Partial<User>): Observable<User> {
    return this.http.put<User>(`${this.apiUrl}/${id}`, user);
  }
}
```

---

## RxJS Best Practices

### Always Unsubscribe
```typescript
// ✅ Good - using takeUntil pattern
private destroy$ = new Subject<void>();

ngOnInit(): void {
  this.dataService.getData()
    .pipe(takeUntil(this.destroy$))
    .subscribe(data => this.data = data);
}

ngOnDestroy(): void {
  this.destroy$.next();
  this.destroy$.complete();
}

// ✅ Alternative - async pipe in template (auto-unsubscribe)
data$ = this.dataService.getData();
// In template: {{ data$ | async }}
```

### Prefer Pipeable Operators
```typescript
// ✅ Good
this.userService.getUsers()
  .pipe(
    map(users => users.filter(u => u.active)),
    catchError(err => {
      console.error('Error loading users', err);
      return of([]);
    })
  )
  .subscribe(activeUsers => this.users = activeUsers);
```

---

## Async/Await

### Prefer Async/Await for Cleaner Code
```typescript
// ✅ Good - async/await
async loadUserData(): Promise<void> {
  try {
    this.isLoading = true;
    const user = await firstValueFrom(this.userService.getUser(this.userId));
    this.user = user;
  } catch (error) {
    console.error('Error loading user', error);
  } finally {
    this.isLoading = false;
  }
}

// ❌ Avoid - callback hell
this.userService.getUser(this.userId).subscribe(user => {
  this.user = user;
  this.userService.getProfile(user.id).subscribe(profile => {
    this.profile = profile;
    // ...more nesting
  });
});
```

---

## Error Handling

### Always Handle Errors
```typescript
// ✅ Good - explicit error handling
this.userService.updateUser(userId, data)
  .pipe(
    catchError(error => {
      this.notificationService.showError('Failed to update user');
      console.error('Update error:', error);
      return EMPTY; // or throwError, or of(fallbackValue)
    })
  )
  .subscribe(result => {
    this.notificationService.showSuccess('User updated');
  });
```

---

## Performance Considerations

### OnPush Change Detection
```typescript
// For presentational components with immutable inputs
@Component({
  selector: 'app-user-card',
  templateUrl: './user-card.component.html',
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class UserCardComponent {
  @Input() user!: User;
}
```

### TrackBy for ngFor
```typescript
// Template
<div *ngFor="let user of users; trackBy: trackByUserId">
  {{ user.name }}
</div>

// Component
trackByUserId(index: number, user: User): string {
  return user.id;
}
```

### Lazy Loading Modules
```typescript
// app-routing.module.ts
const routes: Routes = [
  {
    path: 'library',
    loadChildren: () => import('./library/library.module')
      .then(m => m.LibraryModule)
  }
];
```

---

## Comments

### When to Comment
```typescript
// ✅ Good - explains WHY
// Retry 3 times because API occasionally returns 502 during deployments
retry(3)

// ✅ Good - complex business logic
// Calculate pro-rated subscription cost based on days remaining in billing cycle
const proratedCost = calculateProration(subscription, daysRemaining);

// ❌ Bad - states the obvious
// Increment counter
counter++;

// ❌ Bad - explains WHAT (code should be self-explanatory)
// Loop through users array
users.forEach(user => { });
```

---

## Code Formatting

### Prettier Configuration
```json
{
  "singleQuote": true,
  "trailingComma": "es5",
  "printWidth": 100,
  "tabWidth": 2,
  "semi": true,
  "arrowParens": "avoid"
}
```

**Auto-format on save** in VS Code.

---

## Common Patterns

### Conditional Rendering
```html
<!-- ✅ Good - *ngIf with else -->
<div *ngIf="user; else loading">
  {{ user.name }}
</div>
<ng-template #loading>
  <app-spinner></app-spinner>
</ng-template>
```

### Form Handling
```typescript
// Reactive Forms (preferred)
form = this.fb.group({
  name: ['', Validators.required],
  email: ['', [Validators.required, Validators.email]]
});

onSubmit(): void {
  if (this.form.valid) {
    const formValue = this.form.value;
    // ...
  }
}
```

### HTTP Interceptors
```typescript
// For auth tokens, error handling, etc.
@Injectable()
export class AuthInterceptor implements HttpInterceptor {
  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    const token = this.authService.getToken();
    if (token) {
      req = req.clone({
        setHeaders: { Authorization: `Bearer ${token}` }
      });
    }
    return next.handle(req);
  }
}
```

---

## Resources

- **Angular Style Guide**: https://angular.io/guide/styleguide
- **TypeScript Handbook**: https://www.typescriptlang.org/docs/handbook/intro.html
- **RxJS Documentation**: https://rxjs.dev/
- **Airbnb JavaScript Style Guide**: https://github.com/airbnb/javascript (reference)

---

*Last Updated: November 2025*  
*Version: 1.0*
