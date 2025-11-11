# File Header Standards

## Overview

All source code files in Kinana repositories **must** include a copyright header. This is a requirement for IP protection and licensing compliance.

---

## Copyright Header Template

### Required Header

**All source files** must start with this copyright notice:

```typescript
/**
 * Copyright (c) 2024-2025 Yas Holding Technology - YHT EdTech Division
 * Kinana Content Hub Platform
 * 
 * This code is proprietary and confidential.
 * Unauthorized copying, distribution, or use is strictly prohibited.
 */
```

### Language-Specific Formats

**TypeScript/JavaScript**:
```typescript
/**
 * Copyright (c) 2024-2025 Yas Holding Technology - YHT EdTech Division
 * Kinana Content Hub Platform
 * 
 * This code is proprietary and confidential.
 * Unauthorized copying, distribution, or use is strictly prohibited.
 */

import { Component } from '@angular/core';
// ... rest of file
```

**C#**:
```csharp
/*
 * Copyright (c) 2024-2025 Yas Holding Technology - YHT EdTech Division
 * Kinana Content Hub Platform
 * 
 * This code is proprietary and confidential.
 * Unauthorized copying, distribution, or use is strictly prohibited.
 */

using System;
// ... rest of file
```

**Python**:
```python
# Copyright (c) 2024-2025 Yas Holding Technology - YHT EdTech Division
# Kinana Content Hub Platform
#
# This code is proprietary and confidential.
# Unauthorized copying, distribution, or use is strictly prohibited.

import pandas as pd
# ... rest of file
```

**HTML/CSS**:
```html
<!--
  Copyright (c) 2024-2025 Yas Holding Technology - YHT EdTech Division
  Kinana Content Hub Platform
  
  This code is proprietary and confidential.
  Unauthorized copying, distribution, or use is strictly prohibited.
-->
```

**SQL**:
```sql
-- Copyright (c) 2024-2025 Yas Holding Technology - YHT EdTech Division
-- Kinana Content Hub Platform
--
-- This code is proprietary and confidential.
-- Unauthorized copying, distribution, or use is strictly prohibited.
```

---

## License Information

### Proprietary License

**Kinana is proprietary software**. Source code is:
- Owned by Yas Holding Technology
- Not open source
- Not licensed for redistribution
- Protected as trade secret

### Third-Party Licenses

**Open Source Dependencies**: Tracked in separate license files
- Frontend: `LICENSE-THIRD-PARTY.txt` (npm packages)
- Backend: `LICENSE-THIRD-PARTY.txt` (NuGet packages)
- Python: `requirements-licenses.txt`

**Licensed Frameworks**:
- ABP.io: Commercial multi-developer license
- Nutrient (PSPDF): Annual license
- GDPicture: Included in PSPDF contract

**Reference**: SharePoint F-IP-008 (Third Party License Register)

---

## Author Attribution

### Individual Attribution (Optional)

**Personal attribution discouraged** in proprietary code:
- Code is company-owned intellectual property
- Team collaboration makes individual attribution impractical
- Git history provides complete authorship record

**When to attribute**:
- Research papers or publications
- External contributions (with CLA)
- Significant algorithmic innovations

**Format** (if needed):
```typescript
/**
 * Copyright (c) 2024-2025 Yas Holding Technology - YHT EdTech Division
 * Kinana Content Hub Platform
 * 
 * This code is proprietary and confidential.
 * 
 * Original Algorithm: Dr. Jane Smith (Research Paper XYZ, 2023)
 * Implementation: Kinana Development Team
 */
```

### Team Attribution

Use team-level attribution:
```python
# Copyright (c) 2024-2025 Yas Holding Technology - YHT EdTech Division
# Kinana Content Hub Platform
# Developed by YHT EdTech Division - Kinana Team
```

---

## Function & Method Documentation

### When to Document

**Always**:
- Public APIs (exposed to other modules/services)
- Complex algorithms
- Non-obvious business logic

**Rarely**:
- Simple getters/setters
- Self-explanatory methods
- Internal helper functions

### Format

**TypeScript**:
```typescript
/**
 * Calculates pro-rated subscription amount for partial billing period.
 * 
 * @param subscription - Current subscription details
 * @param startDate - Start date of pro-rated period
 * @param endDate - End date of pro-rated period
 * @returns Pro-rated amount in AED
 * @throws {ValidationError} If dates are invalid
 */
function calculateProRatedAmount(
  subscription: Subscription,
  startDate: Date,
  endDate: Date
): number {
  // Implementation
}
```

**C#**:
```csharp
/// <summary>
/// Calculates pro-rated subscription amount for partial billing period.
/// </summary>
/// <param name="subscription">Current subscription details</param>
/// <param name="startDate">Start date of pro-rated period</param>
/// <param name="endDate">End date of pro-rated period</param>
/// <returns>Pro-rated amount in AED</returns>
/// <exception cref="ValidationException">If dates are invalid</exception>
public decimal CalculateProRatedAmount(
    Subscription subscription,
    DateTime startDate,
    DateTime endDate)
{
    // Implementation
}
```

**Python**:
```python
def calculate_prorated_amount(
    subscription: Subscription,
    start_date: datetime,
    end_date: datetime
) -> float:
    """
    Calculate pro-rated subscription amount for partial billing period.
    
    Args:
        subscription: Current subscription details
        start_date: Start date of pro-rated period
        end_date: End date of pro-rated period
    
    Returns:
        Pro-rated amount in AED
    
    Raises:
        ValueError: If dates are invalid or end_date before start_date
    """
    pass
```

---

## Class & Module Documentation

### Class Documentation

**TypeScript**:
```typescript
/**
 * Copyright (c) 2024-2025 Yas Holding Technology - YHT EdTech Division
 * Kinana Content Hub Platform
 * 
 * This code is proprietary and confidential.
 */

/**
 * Service for managing user subscriptions.
 * 
 * Handles subscription creation, renewal, cancellation, and billing.
 * Integrates with payment gateway and sends subscription notifications.
 */
@Injectable({ providedIn: 'root' })
export class SubscriptionService {
  // Implementation
}
```

**C#**:
```csharp
/*
 * Copyright (c) 2024-2025 Yas Holding Technology - YHT EdTech Division
 * Kinana Content Hub Platform
 * 
 * This code is proprietary and confidential.
 */

/// <summary>
/// Application service for managing user subscriptions.
/// Handles subscription lifecycle, billing, and notifications.
/// </summary>
public class SubscriptionAppService : ApplicationService, ISubscriptionAppService
{
    // Implementation
}
```

### Module/File Documentation

**Python**:
```python
# Copyright (c) 2024-2025 Yas Holding Technology - YHT EdTech Division
# Kinana Content Hub Platform
#
# This code is proprietary and confidential.

"""
Subscription management module for Kinana platform.

This module provides functionality for:
- Subscription creation and renewal
- Billing and payment processing
- Subscription tier management
- Usage tracking and limits enforcement

Dependencies:
    - payment_gateway: For payment processing
    - notification_service: For subscription alerts
"""

from datetime import datetime
from typing import Optional
# ... rest of file
```

---

## README Standards

### Repository README

**Required Sections**:

```markdown
# Kinana [Component Name]

Brief description of component/service.

## Copyright

Copyright (c) 2024-2025 Yas Holding Technology - YHT EdTech Division
This code is proprietary and confidential.

## Overview

What this component does and why it exists.

## Technology Stack

- Framework/Language versions
- Key dependencies
- Infrastructure requirements

## Getting Started

### Prerequisites
- Required tools and versions
- Access requirements

### Installation
```bash
# Clone repository
gh repo clone kinana-ai/kinana-component

# Install dependencies
npm install  # or dotnet restore, pip install -r requirements.txt
```

### Configuration
Environment variables or configuration needed.

### Running Locally
```bash
# Development server
npm start  # or dotnet run, python main.py
```

## Project Structure
```
src/
├── components/
├── services/
└── models/
```

## Development

### Branching Strategy
See [Version Control Standards](../docs/Version_Control_Standards.md)

### Code Standards
See [Coding Standards](../docs/Coding_Standards_Overview.md)

## Testing

Current status: Manual QA (automated testing planned)

### Running Tests (future)
```bash
npm test
```

## Deployment

Automated deployment to staging from `dev` branch.
See [Development Workflow](../docs/Development_Workflow.md)

## Documentation

- API Documentation: `/swagger` (if backend)
- Component Docs: `/docs` folder
- Architecture: `ARCHITECTURE.md` (if complex)

## License

Proprietary - Copyright (c) 2024-2025 Yas Holding Technology

## Contact

For questions or issues, contact the Kinana development team through:
- GitHub Issues (for bugs)
- Microsoft Teams (for discussions)
- Daily Standup (for urgent matters)
```

### Project-Specific README

Adapt template based on component:
- **Frontend**: Angular version, component library
- **Backend**: ABP.io version, database migrations
- **AI**: Python version, model information, GPU requirements

---

## API Documentation Standards

### REST API (Swagger/OpenAPI)

**Auto-generated** from code comments:

```csharp
/// <summary>
/// User management endpoints
/// </summary>
[ApiController]
[Route("api/[controller]")]
public class UsersController : ControllerBase
{
    /// <summary>
    /// Retrieve user by ID
    /// </summary>
    /// <param name="id">User unique identifier</param>
    /// <returns>User details</returns>
    /// <response code="200">User found</response>
    /// <response code="404">User not found</response>
    [HttpGet("{id}")]
    [ProducesResponseType(typeof(UserDto), StatusCodes.Status200OK)]
    [ProducesResponseType(StatusCodes.Status404NotFound)]
    public async Task<ActionResult<UserDto>> GetUser(Guid id)
    {
        // Implementation
    }
}
```

**Access**: `https://staging.kinana.com/swagger`

### GraphQL API (if applicable)

**Schema Documentation**:
```graphql
"""
User account in Kinana platform
"""
type User {
  "Unique identifier"
  id: ID!
  
  "User display name"
  name: String!
  
  "User email address (unique)"
  email: String!
}
```

---

## Enforcement

### Code Review
- **Automated Check**: CI/CD verifies copyright headers (planned)
- **Manual Check**: Reviewers verify headers in new files

### New File Creation
**VS Code Snippet** (recommended):
```json
{
  "Kinana Copyright Header": {
    "prefix": "copyright",
    "body": [
      "/**",
      " * Copyright (c) 2024-2025 Yas Holding Technology - YHT EdTech Division",
      " * Kinana Content Hub Platform",
      " * ",
      " * This code is proprietary and confidential.",
      " * Unauthorized copying, distribution, or use is strictly prohibited.",
      " */"
    ]
  }
}
```

### Bulk Update
**Script to add headers** (if needed):
```bash
# Add copyright header to files missing it
# (Create script in tools/ directory)
```

---

## Resources

**IP Protection**:
- SharePoint IP Governance Repository
- D-IP-007: IP Ownership Matrix
- F-IP-006: Trade Secret Register

**License Management**:
- F-IP-008: Third Party License Register
- PL-IP-002: Open-Source Software Usage Policy

---

*Last Updated: November 2025*  
*Version: 1.0*
