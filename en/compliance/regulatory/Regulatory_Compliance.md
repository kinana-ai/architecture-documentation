# Regulatory Compliance

## Overview

Kinana, like its predecessor AKADIMI will operate in multiple jurisdictions and must comply with data protection and educational regulations in the MINA region, and potentially international markets. This document outlines compliance requirements and implementation approaches.

**Note**: Detailed policies and procedures are maintained in the YHT SharePoint IP Governance repository.

---

## UAE PDPL Compliance

### UAE Personal Data Protection Law (Federal Decree-Law No. 45 of 2021)

**Applicability**: Primary jurisdiction for Kinana operations and data processing

#### Key Requirements

**Data Processing Principles**

- Lawfulness, fairness, and transparency in data processing
- Purpose limitation: Data collected for specific, explicit purposes
- Data minimization: Only collect necessary data
- Accuracy: Keep personal data accurate and up-to-date
- Storage limitation: Retain data only as long as necessary
- Integrity and confidentiality: Appropriate security measures

**Legal Basis for Processing**

- User consent (primary basis for Kinana)
- Contract performance (for platform services)
- Legal obligation compliance
- Legitimate interests (with appropriate safeguards)

**Data Subject Rights**

- Right to access personal data
- Right to rectification of inaccurate data
- Right to erasure ("right to be forgotten")
- Right to restrict processing
- Right to data portability
- Right to object to processing
- Right to withdraw consent

#### Kinana Implementation

**Consent Management (pending implementation)**

- Clear consent mechanisms during user onboarding
- Granular consent options for different data uses
- Easy withdrawal of consent through user settings
- Documented consent records in user database

**Data Protection Measures**

- Encryption at rest and in transit
- Access controls and authentication
- Regular security assessments
- Data breach notification procedures (within 72 hours to authorities)

**User Rights Implementation (pending implementation)**

- Self-service data access through user dashboard
- Data export functionality (JSON format)
- Account deletion process
- Data rectification through profile settings

**Compliance Documentation (pending implementation)**

- Privacy Policy (published on platform)
- Data Processing Records (internal)
- Data Protection Impact Assessment (DPIA) for high-risk processing
- Security policies (SharePoint repository)

---

## Egypt Law 151/2020 Compliance

### Egypt Data Protection Law (Law No. 151 of 2020)

**Applicability**: Required for operations in Egyptian market

#### Key Requirements

**Similar to UAE PDPL with specific considerations**:

- Registration with Egypt Data Protection Centre (for certain data controllers)
- Local data residency requirements for sensitive data
- Arabic language requirements for consent and privacy notices
- Specific requirements for minors' data (parental consent required)

**Cross-Border Data Transfers**

- Transfers to countries with adequate protection mechanisms
- Standard contractual clauses for other jurisdictions
- Explicit consent for transfers without adequacy determination

#### Kinana Implementation

**Applicability**: If Kinana sells and goes to production for Egypt

**Data Localization**

- Azure Middle East region for Egyptian user data
- Consideration of data residency requirements in architecture
- Documentation of data storage locations

**Arabic Language Compliance**

- Privacy Policy available in Arabic
- Consent forms in Arabic
- User interface supports Arabic (native language)

**Minors Protection**

- Age verification mechanisms (educational context)
- Parental consent workflows for under-18 users
- Enhanced privacy protections for student data

**Registration & Reporting**

- Maintain records for potential registration requirement
- Annual compliance reports
- Incident reporting procedures aligned with Egyptian requirements

---

## GDPR Compliance

### General Data Protection Regulation (EU)

**Applicability**: If Kinana expands to EU markets or processes EU resident data

#### Key Requirements

**Higher standard than UAE/Egypt**:

- Stricter consent requirements (freely given, specific, informed, unambiguous)
- Enhanced data subject rights
- Mandatory Data Protection Officer (DPO) appointment (for certain organizations)
- Data Protection Impact Assessments for high-risk processing
- Privacy by Design and by Default

**Data Processing Agreements**

- Required for all third-party processors
- Standard contractual clauses for non-EU transfers
- Regular processor audits

#### Kinana Readiness when implmented

**Current Architecture Supports GDPR**:

- Consent mechanisms exceed minimum requirements
- Data minimization built into platform design
- Strong encryption and security controls
- Comprehensive audit logging
- Data portability functionality
- Right to erasure implementation

**Future Requirements** (if EU expansion):

- Appoint Data Protection Officer
- Conduct comprehensive DPIA
- Update privacy policy for GDPR specifics
- Review and update data processing agreements
- Implement cookie consent management
- Enhanced breach notification procedures

---

## Educational Standards Compliance

### UAE Educational Requirements

**Ministry of Education (MoE) Standards**

**Digital Learning Platform Requirements**:

- Arabic language support mandatory
- Islamic values and cultural appropriateness (relates to content uploaded)
- Alignment with UAE National Curriculum (relates to content uploaded)
- Student data protection enhanced requirements
- Teacher access controls
- Content moderation and filtering

**Implementation in Kinana**:

- RTL (Right-to-Left) Arabic interface
- Content filtering capabilities in Library sub-app
- Role-based access: Students, Teachers, Parents, Administrators
- Curriculum alignment tagging system
- Cultural sensitivity review processes

**Private School Requirements**:

- KHDA (Knowledge and Human Development Authority) compliance for Dubai
- ADEK (Abu Dhabi Department of Education and Knowledge) for Abu Dhabi
- Platform accessibility for students with disabilities

---

## Compliance Implementation Framework

### Technical Controls

**Data Protection**

- Encryption: AES-256 at rest, TLS 1.3 in transit
- Authentication: Multi-factor authentication for admin roles
- Authorization: Role-based access control (RBAC)
- Audit Logging: Comprehensive activity logs retained per legal requirements

**Privacy Controls**

- Consent management system
- Data minimization in data models
- Automated data retention and deletion
- Privacy-preserving analytics (anonymization)

**Security Controls**

- Regular security assessments and penetration testing
- Vulnerability management process
- Incident response procedures (SharePoint: D-IP-006)
- Business continuity and disaster recovery

### Operational Controls

**Policies & Procedures**

- Privacy Policy (published, regularly updated)
- Data Processing Records (internal)
- Third-party data processing agreements
- Employee training and awareness

**Documentation & Records**

- SharePoint repository for all compliance documents
- Regular compliance assessments
- Audit trail for data processing activities
- Incident logs and breach notifications

### Organizational Controls

**Governance Structure**

- Product Manager: Overall compliance responsibility
- Solution Architect: Technical implementation oversight
- Legal Counsel: External advisory (as needed)
- IP Governance Committee: Strategic oversight

**Training & Awareness**

- Annual compliance training for all team members
- Onboarding compliance briefing for new members
- Regular updates on regulatory changes
- Security awareness training

---

## Regulatory Monitoring

### Staying Current

**Regulatory Updates**:

- Monitor UAE Data Protection Office announcements
- Track Egypt Data Protection Centre guidance
- Subscribe to GDPR updates and guidance
- Follow educational ministry policy changes

**Compliance Reviews**:

- Quarterly: Privacy policy review
- Bi-annually: Full compliance assessment
- Annually: Third-party compliance audit (recommended)
- Ongoing: Regulatory change monitoring

---

## Compliance Resources

### Primary References

**UAE**:

- UAE Data Protection Office: https://www.dpo.gov.ae
- Federal Decree-Law No. 45 of 2021 (PDPL)

**Egypt**:

- Egypt Data Protection Centre
- Law No. 151 of 2020

**International**:

- GDPR Official Text: https://gdpr.eu
- Educational standards bodies (MoE UAE, MoE Egypt)

### Internal Resources

**YHT SharePoint - IP Governance Repository**:

- IP Protection Policy (PL-IP-003)
- Third Party License Register (F-IP-008)
- NDA and IP Clauses (D-IP-009)
- Security policies and procedures

**Platform Documentation**:

- Privacy Policy (published on platform)
- Terms of Service (published on platform)
- Data Processing Agreements (for partners/customers)

---

## Compliance Contact Points

**Internal**:

- **Product Manager**: Overall compliance strategy
- **Solution Architect**: Technical compliance implementation
- **Legal Counsel**: External, engaged as needed through CEO

**External**:

- **UAE Data Protection Office**: Regulatory guidance and breach reporting
- **Egypt Data Protection Centre**: Registration and compliance queries
- **Educational Authorities**: Ministry approval and compliance verification

---

_Last Updated: November 2025_  
_Version: 1.0_  
_Note: Detailed compliance policies maintained in SharePoint IP Governance repository_
