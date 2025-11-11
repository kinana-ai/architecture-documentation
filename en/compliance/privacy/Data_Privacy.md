# Data Privacy

## Overview

Data privacy is fundamental to Kinana's operations in educational technology. This document outlines privacy principles, data collection practices, consent management, and data subject rights implementation.

Note: Kinana is in pre-release and consent and data rights management is not yet enabled. The processes outlined below are partially implmented and this is a work in progress.

**Published Privacy Policy**: Available on Kinana platform (updated regularly)  
**Internal Policies**: YHT SharePoint IP Governance repository

---

## Privacy Policy

### Policy Framework

**Location**: Published on Kinana platform, accessible to all users  
**Languages**: English, Arabic  
**Format**: Clear, concise, accessible language suitable for geenral audience

### Policy Content Structure

**1. Introduction & Controller Information**

- Who we are (Ibtikar Edu Tech Solutions / YHT)
- Contact information for privacy inquiries

**2. Data Collection**

- What data we collect (see Data Collection section below)
- Purpose of data collection
- Legal basis for processing

**3. Data Usage**

- How we use collected data
- Analytics and platform improvement
- Communication with users
- Service delivery and support

**4. Data Sharing**

- Third-party service providers (with data processing agreements)
- Legal obligations and law enforcement requests
- Business transfers (if applicable)
- No selling of personal data

**5. Data Security**

- Technical and organizational security measures
- Encryption and access controls
- Employee training and confidentiality

**6. User Rights**

- Comprehensive list of data subject rights
- How to exercise rights
- Response timeframes

**7. Cookies & Tracking**

- Types of cookies used
- Purpose of tracking technologies
- Cookie preferences and opt-out

**8. Children's Privacy**

- Age verification processes
- Parental consent mechanisms
- Enhanced protections for student data

**9. Data Retention**

- Retention periods by data category
- Deletion procedures
- Legal retention requirements

**10. International Transfers**

- Data residency (Azure Middle East regions)
- Safeguards for international transfers
- Standard contractual clauses (if applicable)

**11. Policy Updates**

- How users are notified of changes
- Effective date of updates
- Version history

**12. Contact & Complaints**

- Privacy inquiry contact information
- Complaint procedures
- Regulatory authority contact (UAE Data Protection Office)

### Policy Maintenance

**Review Frequency**: Yearly or when regulatory changes occur  
**Owner**: Product Manager  
**Approval**: Legal review (external counsel) before publication  
**Version Control**: Documented in SharePoint (D-IP-011)

---

## Data Collection

### Data Categories

#### Essential User Data

**Purpose**: Account creation, authentication, platform access

- **User Account Information**:
  - Name (first, last)
  - Email address
  - Username (optional)
  - Password (hashed, never stored in plain text)
  - User role (Student, Teacher, Parent, Administrator)
- **Profile Information**:
  - Grade level (students)
  - Subject areas (teachers / students)
  - Language preference

#### Educational Activity Data

**Purpose**: Learning analytics, progress tracking, content recommendations

- **Content Interaction**:

  - Documents viewed/downloaded (Library sub-app)
  - Videos watched (Videos sub-app)
  - Podcasts listened to (Podcasts sub-app)
  - Brokkly projects created (Visual coding platform)
  - Completion status and progress
  - Time spent on activities

#### Technical Data

**Purpose**: Platform functionality, security, troubleshooting

- **Device & Browser Information**:

  - IP address (anonymized for analytics)
  - Browser type and version
  - Operating system
  - Device type (desktop, mobile, tablet)
  - Screen resolution (for responsive design)

- **Log Data**:
  - Login/logout timestamps
  - Feature usage patterns
  - Error logs and crash reports
  - API calls and response times

#### Communication Data

**Purpose**: Support, notifications, platform communications

- **Support Interactions**:

  - Support ticket content
  - Email correspondence
  - Feedback and survey responses (if implemented)

- **Notifications**:
  - Notification preferences
  - Communication history
  - Email open/click tracking (for platform emails only)

### Data Minimization Principle

**Implemented in Platform Design**:

- Collect only data necessary for specific purposes
- Optional fields for non-essential data
- Anonymous usage where possible (aggregated analytics)
- Regular review of data collection practices

### Data Sources

**Direct Collection**:

- User registration and profile setup
- User-generated content (projects, uploads)
- User interactions with platform features

**Automated Collection**:

- Technical logs and analytics
- Session information
- Error tracking and monitoring

**Third-Party Sources**:

- None (all data collected directly from users or system logs)

---

## User Consent

### Consent Mechanisms

#### Registration Consent

**When**: Initial account creation

**Consent Items**:

- ✓ Terms of Service agreement
- ✓ Privacy Policy acknowledgment
- ✓ Essential data processing (required for service)
- ✓ Communication preferences (optional)
- ✓ Analytics and improvement (optional)

**Implementation**:

- Clear checkboxes for each consent item
- Links to full policies (not hidden in fine print)
- Separate checkboxes for optional vs. required consent
- Cannot proceed without required consents

#### Ongoing Consent Management

**Where**: User account settings / privacy preferences

**User Control**:

- View current consent status
- Modify communication preferences
- Opt in/out of optional data processing
- Withdraw consent for non-essential processing

**Granular Consent Options**:

- Email notifications (by category)
- Analytics and usage data
- Personalized content recommendations
- Third-party integrations (if applicable)

### Consent Records

**Documentation**:

- Timestamp of consent
- Type of consent given
- User identifier
- Version of privacy policy/terms accepted
- IP address (for verification)

**Storage**: Secure database, encrypted at rest  
**Retention**: Duration of user account + legal retention period  
**Audit**: Available for regulatory compliance verification

### Withdrawal of Consent

**User Rights**:

- Easy withdrawal through account settings
- Clear indication of consequences (e.g., service limitations)
- Immediate effect (or within 24 hours for technical processing)

**Implementation**:

- "Withdraw consent" buttons in privacy settings
- Confirmation dialog explaining impact
- Processing queue for consent withdrawal requests
- Automated data deletion workflows (where applicable)

---

## Data Subject Rights

### Rights Implementation

#### 1. Right to Access

**Request Type**: User wants to know what data we hold

**Implementation**:

- Self-service data export in account settings
- Export format: JSON (machine-readable)
- Includes all personal data and activity history
- Generated within minutes, available for download

**Process**:

1. User requests data export through dashboard
2. System compiles all user data
3. Export file generated and encrypted
4. Download link sent via email (expires in 7 days)
5. User downloads and decrypts with account password

#### 2. Right to Rectification

**Request Type**: User wants to correct inaccurate data

**Implementation**:

- Self-service through profile settings
- Most fields editable directly by user
- Restricted fields (e.g., email) require verification
- Audit trail of modifications

**Process**:

1. User updates data in profile settings
2. Changes validated (format, uniqueness)
3. Verification required for sensitive changes (email, password)
4. Updated immediately in database
5. Confirmation notification sent

#### 3. Right to Erasure ("Right to be Forgotten")

**Request Type**: User wants to delete their account and data

**Implementation**:

- "Delete Account" option in account settings
- Clear explanation of consequences (irreversible)
- Confirmation required (re-enter password)
- Grace period (30 days) before permanent deletion

**Process**:

1. User initiates account deletion
2. Account deactivated immediately (login disabled)
3. 30-day grace period for user to cancel deletion
4. After grace period: permanent data deletion
5. Retention of minimal data for legal requirements only

**Exceptions** (data retained despite erasure request):

- Legal obligations (accounting, audit)
- Fraud prevention and security
- Anonymized aggregated data (cannot identify individual)

#### 4. Right to Restrict Processing

**Request Type**: User wants to limit how data is used

**Implementation**:

- Granular processing preferences in account settings
- Opt-out of analytics
- Opt-out of personalization
- Opt-out of communications

**Process**:

1. User adjusts processing preferences
2. Flags set in user profile
3. System respects flags in all processing operations
4. Regular verification of compliance

#### 5. Right to Data Portability

**Request Type**: User wants to transfer data to another service

**Implementation**:

- Same mechanism as Right to Access
- Standardized JSON format
- Includes all user-generated content
- Machine-readable for import to other systems

**Scope**:

- All personal data provided by user
- User-generated content (projects, uploads)
- Activity history and progress data

#### 6. Right to Object

**Request Type**: User objects to specific processing activities

**Implementation**:

- Objection form in privacy settings
- Review by Product Manager for legitimate grounds
- Response within 30 days
- Processing halted or explanation provided

**Grounds for Objection**:

- Processing based on legitimate interests
- Direct marketing (always honored)
- Profiling and automated decision-making

#### 7. Right to Withdraw Consent

**Request Type**: User withdraws previously given consent

**Implementation**: See "Withdrawal of Consent" section above

### Rights Request Handling

**Response Timeframes**:

- Acknowledge request: Within 3 business days
- Fulfill request: Within 30 days (UAE/Egypt/GDPR standard)
- Complex requests: May extend to 60 days with explanation

**Verification**:

- User must be logged into account, OR
- Email verification for requests submitted externally
- Additional verification for sensitive requests

**Communication**:

- All responses via secure email
- Clear explanation of actions taken
- Information about complaint procedures if unsatisfied

### Rights Request Tracking

**System**:

- Internal ticketing system for rights requests
- Status tracking (received, in progress, completed)
- Audit log of all rights exercises
- Reporting dashboard for compliance monitoring

**Metrics Tracked**:

- Number of requests by type
- Response times
- Fulfillment rates
- Complaints or escalations

---

## Privacy by Design

### Architectural Principles

**Data Minimization**:

- Collect only necessary data
- Default to minimal data sharing
- Regular review of data collection needs

**Privacy Controls**:

- Built-in consent management
- Granular privacy preferences
- Easy access to privacy tools

**Security First**:

- Encryption by default
- Secure authentication
- Regular security assessments

**Transparency**:

- Clear privacy policy
- Accessible privacy settings
- Audit trail for data processing

---

## Data Retention & Deletion

### Retention Periods

**Active User Data**:

- Retained while account is active
- Regular backups (encrypted)
- User can request deletion anytime

**Deleted Account Data**:

- 30-day grace period (soft delete)
- Permanent deletion after grace period
- Legal retention exceptions

**System Logs**:

- Security logs: 2 years
- Access logs: 1 year
- Error logs: 90 days
- Anonymized analytics: Indefinitely

**Legal Retention**:

- Accounting records: 7 years (UAE requirement)
- Contractual data: Duration of contract + 6 years
- Dispute-related data: Until resolution + 1 year

### Automated Deletion

**Inactive Accounts**:

- Warning after 2 years of inactivity
- Deletion after 3 years if no response
- Email notifications before deletion

**System Process**:

- Daily cron job checks for expired data
- Automated deletion workflows
- Verification and logging of deletions
- Irreversible secure deletion (data overwriting)

---

## Privacy Resources

**Internal**:

- SharePoint IP Governance repository (policies and procedures)
- Platform Privacy Policy (published)
- Privacy training materials (Corporate HR)

**External**:

- UAE Data Protection Office: https://www.dpo.gov.ae
- Egypt Data Protection Centre
- GDPR guidance: https://gdpr.eu

**Contacts**:

- **Privacy Inquiries**: Product Manager
- **Data Rights Requests**: Through platform privacy settings or email
- **Complaints**: UAE Data Protection Office or Egypt Data Protection Centre

---

_Last Updated: November 2025_  
_Version: 1.0_  
_Note: Published Privacy Policy available on Kinana platform_
