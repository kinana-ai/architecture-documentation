# Kinana Platform - Quick Reference Guide

## Essential Commands

### Kubernetes Operations

#### View Services
```bash
# List all pods
kubectl get pods -n kinana-dev

# List all services
kubectl get services -n kinana-dev

# List ingress resources
kubectl get ingress -n kinana-dev

# Get detailed info
kubectl describe pod <pod-name> -n kinana-dev
```

#### View Logs
```bash
# Tail logs
kubectl logs -f <pod-name> -n kinana-dev

# View logs from all pods with label
kubectl logs -l app=api -n kinana-dev

# Previous pod logs
kubectl logs <pod-name> -n kinana-dev --previous
```

#### Scaling
```bash
# Manual scale
kubectl scale deployment api --replicas=5 -n kinana-dev

# Check autoscaler
kubectl get hpa -n kinana-dev

# Edit deployment
kubectl edit deployment api -n kinana-dev
```

### Database Operations

#### MySQL (FSDB)
```bash
# Connect to MySQL
kubectl exec -it fsdb-pod -n kinana-dev -- mysql -u root -p

# Backup database
kubectl exec fsdb-pod -n kinana-dev -- \
  mysqldump -u root -p kinana_db > backup.sql

# Check table sizes
SELECT 
  table_name,
  ROUND(data_length / 1024 / 1024, 2) AS data_mb
FROM information_schema.tables
WHERE table_schema = 'kinana_db';
```

#### Redis
```bash
# Connect to Redis
kubectl exec -it cache-pod -n kinana-dev -- redis-cli

# Check memory usage
INFO memory

# List all keys (be careful in production!)
KEYS *

# Get specific key
GET session:user123
```

### Certificate Management

```bash
# List certificates
kubectl get certificates -n kinana-dev

# Check certificate details
kubectl describe certificate kinana-api-secret -n kinana-dev

# Force certificate renewal
kubectl delete secret kinana-api-secret -n kinana-dev
```

### Storage Operations

```bash
# List persistent volumes
kubectl get pv

# List persistent volume claims
kubectl get pvc -n kinana-dev

# Check storage usage
kubectl describe pvc kinana-files-dev -n kinana-dev
```

## Service Endpoints

### Core Services
| Service | Internal URL | External URL |
|---------|--------------|--------------|
| Identity | http://id.kinana-dev.svc.cluster.local | https://id.kinana.ai |
| API Gateway | http://api.kinana-dev.svc.cluster.local | https://api.kinana.ai |
| Admin | http://admin.kinana-dev.svc.cluster.local | https://admin.kinana.ai |
| Cache (Redis) | cache.kinana-dev.svc.cluster.local:6379 | N/A (internal) |
| FSDB (MySQL) | fsdb.kinana-dev.svc.cluster.local:3306 | N/A (internal) |

### Application Services
| Service | External URL |
|---------|--------------|
| Main App | https://app.kinana.ai |
| PDF Optimization | https://pdfopt.kinana.ai |
| PDF Translation | https://pdftra.kinana.ai |
| Language Translation | https://kintra.kinana.ai |
| PDF Images | https://pdfimg.kinana.ai |
| Marketing Site | https://www.kinana.ai |

### LTI Services
| Service | External URL |
|---------|--------------|
| LTI Main | https://xwinji.lti.kinana.ai |
| LTI PAAET | https://readerapp.lti.kinana.ai |

## Connection Strings

### MySQL (FSDB)
```
Host: fsdb.kinana-dev.svc.cluster.local
Port: 3306
Database: kinana_db
User: root
Password: [from environment]
```

### SQL Server (LTI)
```
Server: 10.7.0.4,1433
Database: lti_db
User: akadimi
Password: [from Azure Key Vault]
Encrypt: true
TrustServerCertificate: true
```

### Redis
```
Host: cache.kinana-dev.svc.cluster.local
Port: 6379
Password: [none in development]
```

### Azure Blob Storage
```
Account: kinanadevsto
Connection String: [from Azure Key Vault]
Containers:
  - kinanafiles
  - kinanadocuments
  - kinanarawdocuments
```

## Environment Variables

### Common (.NET Services)
```bash
REDIS=cache
ASPNETCORE_URLS=http://+:80
APP_ENV=production
```

### LTI Services
```bash
PORT=3001
HOST=0.0.0.0
PRODUCTION=true
CACHE_TTL=3600
SCOPE=openid
CONSUMER_KEY=Akadimi
MSSQL_HOST=10.7.0.4
MSSQL_PORT=1433
MSSQL_ENCRYPT=true
MSSQL_TRUST_SERVER_CERTIFICATE=true
```

## API Quick Reference

### Authentication
```bash
# Login
curl -X POST https://api.kinana.ai/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"user@example.com","password":"password"}'

# Refresh token
curl -X POST https://api.kinana.ai/auth/refresh \
  -H "Content-Type: application/json" \
  -d '{"refresh_token":"<token>"}'
```

### Files
```bash
# List files
curl -X GET https://api.kinana.ai/files \
  -H "Authorization: Bearer <token>"

# Upload file
curl -X POST https://api.kinana.ai/files \
  -H "Authorization: Bearer <token>" \
  -F "file=@document.pdf"

# Download file
curl -X GET https://api.kinana.ai/files/<id>/download \
  -H "Authorization: Bearer <token>" \
  -o downloaded-file.pdf
```

## Troubleshooting Quick Fixes

### Pod Won't Start
```bash
# Check events
kubectl describe pod <pod-name> -n kinana-dev

# Check logs
kubectl logs <pod-name> -n kinana-dev

# Common fixes:
# - Check image pull secrets
# - Verify resource requests/limits
# - Check persistent volume claims
```

### Service Not Accessible
```bash
# Check service
kubectl get svc <service-name> -n kinana-dev

# Check endpoints
kubectl get endpoints <service-name> -n kinana-dev

# Check ingress
kubectl describe ingress -n kinana-dev

# Test from within cluster
kubectl run -it --rm debug --image=busybox --restart=Never -- \
  wget -qO- http://api.kinana-dev.svc.cluster.local
```

### Certificate Issues
```bash
# Check certificate status
kubectl get certificate <cert-name> -n kinana-dev

# Check certificate details
kubectl describe certificate <cert-name> -n kinana-dev

# View certificate secret
kubectl get secret <cert-secret> -n kinana-dev -o yaml

# Delete and recreate (cert-manager will renew)
kubectl delete certificate <cert-name> -n kinana-dev
kubectl delete secret <cert-secret> -n kinana-dev
```

### Database Connection Issues
```bash
# Test MySQL connection
kubectl run -it --rm mysql-test --image=mysql:8.0 --restart=Never -- \
  mysql -h fsdb.kinana-dev.svc.cluster.local -u root -p

# Test Redis connection
kubectl run -it --rm redis-test --image=redis:6.0.8 --restart=Never -- \
  redis-cli -h cache.kinana-dev.svc.cluster.local ping
```

## Monitoring Queries

### Prometheus Queries
```promql
# CPU usage by pod
sum(rate(container_cpu_usage_seconds_total{namespace="kinana-dev"}[5m])) by (pod)

# Memory usage by pod
sum(container_memory_usage_bytes{namespace="kinana-dev"}) by (pod)

# Pod restart count
sum(kube_pod_container_status_restarts_total{namespace="kinana-dev"}) by (pod)

# Request rate
sum(rate(nginx_ingress_controller_requests[5m])) by (host)
```

### Log Analytics (KQL)
```kusto
// Recent errors
ContainerLog
| where Namespace == "kinana-dev"
| where LogEntry contains "error" or LogEntry contains "exception"
| project TimeGenerated, ContainerName, LogEntry
| order by TimeGenerated desc
| take 100

// Pod restarts
KubePodInventory
| where Namespace == "kinana-dev"
| where RestartCount > 0
| summarize LastRestart=max(TimeGenerated) by Name, RestartCount
| order by RestartCount desc
```

## Important URLs

### Azure Resources
- **AKS Cluster**: [Azure Portal - Kubernetes services]
- **Container Registry**: https://portal.azure.com - uepcr.azurecr.io
- **Key Vault**: https://portal.azure.com - ibt-prd-kv-01
- **Storage Account**: kinanadevsto

### Documentation
- **Kubernetes Docs**: https://kubernetes.io/docs/
- **Azure Docs**: https://docs.microsoft.com/azure/
- **NGINX Ingress**: https://kubernetes.github.io/ingress-nginx/
- **cert-manager**: https://cert-manager.io/docs/

### Tools
- **kubectl Cheat Sheet**: https://kubernetes.io/docs/reference/kubectl/cheatsheet/
- **Azure CLI**: https://docs.microsoft.com/cli/azure/
- **Lens IDE**: https://k8slens.dev/

## Emergency Contacts

| Role | Responsibility | Contact Method |
|------|----------------|----------------|
| Platform Lead | Overall platform | [Contact Info] |
| DevOps Lead | Infrastructure | [Contact Info] |
| Security Lead | Security incidents | [Contact Info] |
| On-Call Engineer | 24/7 support | [Contact Info] |

## Critical Thresholds

### Alerts
| Metric | Warning | Critical |
|--------|---------|----------|
| CPU Usage | > 70% | > 90% |
| Memory Usage | > 75% | > 90% |
| Disk Usage | > 80% | > 95% |
| Pod Restarts | > 5 in 1h | > 10 in 1h |
| Error Rate | > 1% | > 5% |
| Response Time | > 500ms | > 2s |

---

**Last Updated**: November 19, 2024
**Version**: 1.0
