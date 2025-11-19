# Security Architecture Overview

## Introduction

The Kinana Platform implements comprehensive security measures across all architectural layers to protect data, ensure privacy, and maintain system integrity. This document outlines the security architecture, principles, and implementations.

## Security Principles

### 1. Defense in Depth
Multiple layers of security controls throughout the system:
- Network security (Ingress/TLS)
- Application security (Authentication/Authorization)
- Data security (Encryption)
- Infrastructure security (Kubernetes/Azure)

### 2. Least Privilege
- Users and services granted minimum necessary permissions
- Role-based access control (RBAC)
- Service account isolation
- Just-in-time access for administrative tasks

### 3. Zero Trust
- Never trust, always verify
- Continuous authentication and authorization
- Network segmentation
- Encrypted communications

### 4. Security by Design
- Security considerations in all development phases
- Threat modeling during design
- Secure coding practices
- Regular security audits

## Security Layers

### Layer 1: Network Security

#### TLS/SSL Encryption
- **All external traffic**: TLS 1.2+ enforced
- **Certificate management**: Automated via cert-manager
- **Certificate provider**: Let's Encrypt
- **Certificate rotation**: Automatic before expiration

```
User → HTTPS (TLS 1.2+) → NGINX Ingress → Internal HTTP
```

#### Ingress Security
**NGINX Ingress Controller Configuration:**
```yaml
# Global security headers
nginx.ingress.kubernetes.io/configuration-snippet: |
  more_set_headers "X-Frame-Options: SAMEORIGIN";
  more_set_headers "X-Content-Type-Options: nosniff";
  more_set_headers "X-XSS-Protection: 1; mode=block";
  more_set_headers "Strict-Transport-Security: max-age=31536000";
```

**Features:**
- HSTS (HTTP Strict Transport Security)
- XSS Protection headers
- Content type sniffing prevention
- Clickjacking protection

---

### Layer 2: Application Security

#### Authentication

**Identity Service:**
- OAuth 2.0 / OpenID Connect
- JWT (JSON Web Tokens)
- Multi-factor authentication (MFA) support
- Session management via Redis

**Token Structure:**
```json
{
  "iss": "https://id.kinana.ai",
  "sub": "user-uuid",
  "aud": "kinana-api",
  "exp": 1700000000,
  "iat": 1699996400,
  "roles": ["student", "user"],
  "tenant": "tenant_id"
}
```

**Token Lifecycle:**
- **Access Token**: 1 hour lifetime
- **Refresh Token**: 30 days lifetime
- **Revocation**: Immediate via Redis blacklist

#### Authorization

**Role-Based Access Control (RBAC):**
```
User → Role → Permissions → Resources
```

**Standard Roles:**
| Role | Description | Permissions |
|------|-------------|-------------|
| Super Admin | Platform administrator | All permissions |
| Tenant Admin | Organization administrator | Manage organization users and content |
| Instructor | Course instructor | Create/manage courses and grade students |
| Student | Course participant | Access courses, submit assignments |
| Guest | Limited access | View public content only |

**Permission Model:**
```
{resource}:{action}

Examples:
- files:read
- files:write
- courses:create
- users:manage
- grades:submit
```

#### API Security

**API Gateway Protection:**
1. **Rate Limiting**
   ```
   100 requests per minute per user
   1000 requests per minute per tenant
   ```

2. **Request Validation**
   - Schema validation
   - Input sanitization
   - SQL injection prevention
   - XSS prevention

3. **API Keys**
   - Service-to-service authentication
   - Key rotation every 90 days
   - Scoped permissions

---

### Layer 3: Data Security

#### Encryption

**At Rest:**
- **Azure Blob Storage**: AES-256 encryption
- **Databases**: Transparent Data Encryption (TDE)
- **Secrets**: Azure Key Vault encryption

**In Transit:**
- **External**: TLS 1.2+
- **Internal**: Optional mTLS via service mesh
- **Database connections**: Encrypted connections

#### Data Classification

| Level | Description | Security Controls |
|-------|-------------|-------------------|
| Public | Public information | Standard encryption |
| Internal | Internal use only | Encryption + access control |
| Confidential | Sensitive data | Encryption + strict access control + audit logging |
| Restricted | Highly sensitive | Encryption + MFA + approval workflow + detailed audit |

#### Data Protection

**Personal Data (GDPR):**
- Data minimization
- Purpose limitation
- Storage limitation
- Data subject rights (access, deletion, portability)

**Sensitive Data:**
- Field-level encryption for PII
- Tokenization for sensitive identifiers
- Data masking in logs
- Secure deletion procedures

---

### Layer 4: Infrastructure Security

#### Kubernetes Security

**Pod Security:**
```yaml
securityContext:
  runAsNonRoot: true
  runAsUser: 1000
  fsGroup: 2000
  capabilities:
    drop:
      - ALL
  readOnlyRootFilesystem: true
```

**Network Policies:**
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: api-network-policy
spec:
  podSelector:
    matchLabels:
      app: api
  policyTypes:
    - Ingress
    - Egress
  ingress:
    - from:
      - podSelector:
          matchLabels:
            app: ingress-nginx
  egress:
    - to:
      - podSelector:
          matchLabels:
            app: cache
      - podSelector:
          matchLabels:
            app: fsdb
```

**RBAC in Kubernetes:**
- Service accounts per service
- Namespace isolation
- Minimal ClusterRole permissions

#### Container Security

**Image Security:**
- Scan images for vulnerabilities (Azure Container Registry)
- Use official base images
- Minimal image layers
- No secrets in images

**Image Signing:**
```bash
# Sign images
docker trust sign uepcr.azurecr.io/kinanaapi:1.0.0

# Verify signatures
docker trust inspect --pretty uepcr.azurecr.io/kinanaapi:1.0.0
```

---

## Secret Management

### Azure Key Vault

**Purpose**: Centralized secret management

**Stored Secrets:**
- Database passwords
- API keys
- TLS certificates
- Service credentials
- Encryption keys

**Access Control:**
- Managed identities for Azure resources
- RBAC policies
- Audit logging
- Secret rotation policies

**Secret Rotation:**
```
Database credentials: 90 days
API keys: 90 days
Certificates: Automatic via cert-manager
Encryption keys: Annual rotation
```

### Kubernetes Secrets

**Usage:**
- Container registry credentials
- TLS certificates
- Service account tokens

**Best Practices:**
- Never commit secrets to Git
- Use external secrets operator
- Encrypt secrets at rest (etcd encryption)
- Limit secret access via RBAC

---

## Authentication & Authorization Flows

### User Authentication Flow

```
1. User → Login Request → Identity Service
2. Identity Service → Validate Credentials → User Database
3. Identity Service → Generate JWT → User
4. User → API Request + JWT → API Gateway
5. API Gateway → Validate JWT → Identity Service
6. API Gateway → Check Permissions → Continue or Deny
```

### LTI Authentication Flow

```
1. LMS → LTI Launch → Kinana LTI Service
2. LTI Service → Validate Launch → Check Signature
3. LTI Service → Create Session → SQL Server
4. LTI Service → Issue Token → Application
5. Application → Validate Token → Identity Service
6. Application → Grant Access → User
```

## Security Monitoring

### Audit Logging

**What to Log:**
- Authentication attempts (success/failure)
- Authorization decisions
- Data access (create, read, update, delete)
- Administrative actions
- Security events (anomalies, threats)

**Log Format:**
```json
{
  "timestamp": "2024-11-19T08:00:00Z",
  "event_type": "authentication",
  "action": "login_success",
  "user_id": "user-uuid",
  "ip_address": "192.168.1.100",
  "user_agent": "Mozilla/5.0...",
  "tenant_id": "tenant_001"
}
```

**Log Retention:**
- Security logs: 1 year
- Audit logs: 7 years (compliance)
- Access logs: 90 days

### Security Monitoring Tools

**Recommended Stack:**
- **Azure Security Center**: Cloud security posture
- **Azure Sentinel**: SIEM (Security Information and Event Management)
- **Falco**: Kubernetes runtime security
- **Prometheus + Grafana**: Metrics and alerting

**Key Metrics:**
- Failed authentication attempts
- Unusual access patterns
- Certificate expiration dates
- Vulnerability scan results
- Security policy violations

---

## Incident Response

### Security Incident Classification

| Severity | Description | Response Time |
|----------|-------------|---------------|
| Critical | Data breach, system compromise | Immediate (< 1 hour) |
| High | Attempted breach, service disruption | 4 hours |
| Medium | Security policy violation | 24 hours |
| Low | Minor security issue | 72 hours |

### Incident Response Process

1. **Detection & Analysis**
   - Identify security event
   - Assess severity
   - Contain threat

2. **Containment**
   - Isolate affected systems
   - Prevent spread
   - Preserve evidence

3. **Eradication**
   - Remove threat
   - Patch vulnerabilities
   - Update security controls

4. **Recovery**
   - Restore services
   - Verify security
   - Monitor for recurrence

5. **Post-Incident**
   - Document incident
   - Lessons learned
   - Update procedures

---

## Compliance & Standards

### Standards Compliance

**GDPR (General Data Protection Regulation):**
- Data protection by design
- Right to erasure
- Data portability
- Breach notification

**ISO 27001:**
- Information security management
- Risk assessment
- Security controls
- Continuous improvement

**SOC 2:**
- Security
- Availability
- Processing integrity
- Confidentiality
- Privacy

### Security Certifications

**Target Certifications:**
- ISO 27001 (Information Security Management)
- SOC 2 Type II (Service Organization Controls)
- PCI DSS (if handling payment data)

---

## Security Best Practices

### Development Security

**Secure Coding:**
- Input validation
- Output encoding
- Parameterized queries
- Error handling without information disclosure

**Code Review:**
- Peer review for all code changes
- Security-focused review for critical components
- Automated security scanning

**Dependency Management:**
- Regular dependency updates
- Vulnerability scanning
- Software composition analysis

### Operational Security

**Access Management:**
- Principle of least privilege
- Regular access reviews
- Just-in-time access for administrative tasks
- MFA for all administrative access

**Patch Management:**
- Regular security updates
- Automated patching for non-critical systems
- Change management for production

**Backup Security:**
- Encrypted backups
- Offsite backup storage
- Regular restore testing
- Access controls on backups

---

## Future Security Enhancements

### Planned Improvements

1. **Service Mesh (Istio/Linkerd)**
   - Mutual TLS between services
   - Fine-grained traffic policies
   - Advanced observability

2. **Web Application Firewall (WAF)**
   - OWASP Top 10 protection
   - Bot detection
   - DDoS mitigation
   - Geo-blocking

3. **Security Information and Event Management (SIEM)**
   - Centralized log aggregation
   - Real-time threat detection
   - Automated response

4. **Vulnerability Management**
   - Continuous scanning
   - Automated remediation
   - Risk scoring

5. **Zero Trust Architecture**
   - Device trust
   - User trust
   - Application trust
   - Data trust

---

**Document Version**: 1.0  
**Last Updated**: November 2024  
**Classification**: Unclassified
