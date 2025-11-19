# Infrastructure

## Overview

The Kinana Platform is deployed on Microsoft Azure using Azure Kubernetes Service (AKS) as the primary orchestration platform. This document details the infrastructure components, configuration, and operational procedures.

## Azure Kubernetes Service (AKS)

### Cluster Configuration

| Property | Value |
|----------|-------|
| Cloud Provider | Microsoft Azure |
| Region | (To be specified based on deployment) |
| Kubernetes Version | 1.27+ |
| Node OS | Linux (Ubuntu 24.04) |
| Network Plugin | Azure CNI |
| Network Policy | Calico |

### Node Pools

#### System Node Pool
```yaml
Name: systempool
VM Size: Standard_D4s_v3
  - vCPUs: 4
  - RAM: 16 GB
  - Disk: 128 GB Premium SSD
Node Count: 3
Auto-scaling: Enabled (3-5 nodes)
Purpose: System pods (kube-system, ingress-nginx)
```

#### Application Node Pool
```yaml
Name: apppool
VM Size: Standard_D8s_v3
  - vCPUs: 8
  - RAM: 32 GB
  - Disk: 256 GB Premium SSD
Node Count: 3
Auto-scaling: Enabled (3-10 nodes)
Purpose: Application workloads
```

### Cluster Networking

**Network Configuration:**
```yaml
Service CIDR: 10.0.0.0/16
Pod CIDR: 10.244.0.0/16
DNS Service IP: 10.0.0.10
Docker Bridge CIDR: 172.17.0.1/16
```

**Load Balancer:**
- Type: Azure Load Balancer (Standard SKU)
- Static Public IP
- DDoS Protection: Basic

---

## Kubernetes Components

### Namespaces

#### kinana-dev
**Purpose**: Production application workloads

**Resources:**
- Application services
- Databases (Redis, MySQL)
- Ingress resources
- Certificates
- Persistent Volume Claims

**Resource Quotas:**
```yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: kinana-dev-quota
  namespace: kinana-dev
spec:
  hard:
    requests.cpu: "50"
    requests.memory: 100Gi
    limits.cpu: "100"
    limits.memory: 200Gi
    persistentvolumeclaims: "20"
    services.loadbalancers: "2"
```

#### akadimi-stg
**Purpose**: Legacy storage and staging

**Resources:**
- Legacy persistent volumes
- Migration artifacts
- Archived data

#### kube-system
**Purpose**: Kubernetes system components

**Key Pods:**
- CoreDNS
- Metrics Server
- Azure CSI drivers
- Cluster Autoscaler

#### ingress-nginx
**Purpose**: NGINX Ingress Controller

**Configuration:**
```yaml
controller:
  replicaCount: 3
  resources:
    requests:
      cpu: 100m
      memory: 90Mi
    limits:
      cpu: 1000m
      memory: 500Mi
  service:
    type: LoadBalancer
    externalTrafficPolicy: Local
```

#### cert-manager
**Purpose**: Certificate management

**Components:**
- cert-manager controller
- cert-manager webhook
- cert-manager cainjector

**ClusterIssuer:**
```yaml
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: letsencrypt-prod
spec:
  acme:
    server: https://acme-v02.api.letsencrypt.org/directory
    email: admin@kinana.ai
    privateKeySecretRef:
      name: letsencrypt-prod
    solvers:
    - http01:
        ingress:
          class: nginx
```

---

## Storage Infrastructure

### Azure Blob Storage

**Storage Accounts:**

#### kinanadevsto (Development/Production)
```yaml
Performance: Premium
Replication: Zone-Redundant Storage (ZRS)
Secure Transfer: Required
Minimum TLS: 1.2
Access Tier: Hot
Containers:
  - kinanafiles
  - kinanadocuments
  - kinanarawdocuments
```

#### akadimistore (Legacy)
```yaml
Performance: Standard
Replication: Locally-Redundant Storage (LRS)
Access Tier: Cool (archived data)
Containers:
  - medias
  - vectors
  - books
  - media-resources
```

### Persistent Volumes

**Storage Class:**
```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: azureblob-fuse-retain-premium
provisioner: blob.csi.azure.com
parameters:
  skuName: Premium_LRS
reclaimPolicy: Retain
volumeBindingMode: Immediate
allowVolumeExpansion: true
```

**Persistent Volume Claims:**
```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: kinana-files-dev
  namespace: kinana-dev
spec:
  accessModes:
    - ReadWriteMany
  storageClassName: azureblob-fuse-retain-premium
  resources:
    requests:
      storage: 10Gi
```

---

## Container Registry

### Azure Container Registry (ACR)

**Registry Details:**
```yaml
Name: uepcr
URL: uepcr.azurecr.io
SKU: Standard
Admin Account: Disabled (use AAD)
Geo-replication: Disabled
Webhooks: Configured for CI/CD
```

**Security:**
- Azure AD authentication
- Role-based access control
- Vulnerability scanning enabled
- Content trust enabled

**Image Retention:**
```yaml
Untagged manifests: 7 days
Tagged images: 90 days
Dev images (*_dev): 30 days
Production images: Indefinite
```

---

## Networking

### Ingress Configuration

**NGINX Ingress Controller:**
```yaml
Global Configuration:
  proxy-body-size: 1500M
  client-max-body-size: 2G
  proxy-read-timeout: 600
  proxy-send-timeout: 600
  server-snippet: |
    underscores_in_headers on;
  
SSL Configuration:
  ssl-protocols: TLSv1.2 TLSv1.3
  ssl-ciphers: HIGH:!aNULL:!MD5
  ssl-prefer-server-ciphers: "on"
```

**Ingress Resources:**
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: kinana-api
  namespace: kinana-dev
  annotations:
    cert-manager.io/cluster-issuer: letsencrypt-prod
    nginx.ingress.kubernetes.io/proxy-body-size: 1500M
spec:
  ingressClassName: nginx
  tls:
  - hosts:
    - api.kinana.ai
    secretName: kinana-api-secret
  rules:
  - host: api.kinana.ai
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: api
            port:
              number: 80
```

### DNS Configuration

**Azure DNS Zones:**
```
kinana.ai
  - A: www → Load Balancer IP
  - A: api → Load Balancer IP
  - CNAME: *.app → Load Balancer DNS
  - CNAME: *.admin → Load Balancer DNS
  - CNAME: *.id → Load Balancer DNS
```

**TTL Settings:**
- Production records: 300 seconds (5 minutes)
- Wildcard records: 600 seconds (10 minutes)

---

## Security Infrastructure

### Azure Key Vault

**Key Vault Details:**
```yaml
Name: ibt-prd-kv-01
SKU: Premium
Soft Delete: Enabled (90 days)
Purge Protection: Enabled
```

**Secrets:**
- Database passwords
- API keys
- Service credentials
- Legacy SSL certificates

**Access Policies:**
```yaml
AKS Managed Identity:
  Permissions:
    - Get (secrets)
    - List (secrets)
Admin Users:
  Permissions:
    - All (secrets, keys, certificates)
```

### Network Security

**Network Security Groups (NSG):**
```yaml
AKS Subnet NSG:
  Inbound Rules:
    - Allow HTTPS from Internet
    - Allow SSH from Management Subnet
    - Allow Kubernetes API from Management
  Outbound Rules:
    - Allow All (application outbound)
```

**Azure Firewall (Future):**
- Application rules
- Network rules
- Threat intelligence

---

## Monitoring and Logging

### Azure Monitor

**Container Insights:**
```yaml
Enabled: Yes
Workspace: kinana-log-analytics
Retention: 90 days
Alert Rules:
  - Pod CPU > 80% for 5 minutes
  - Pod Memory > 80% for 5 minutes
  - Pod Crash Loop
  - Node Not Ready
```

**Metrics:**
- CPU utilization
- Memory utilization
- Disk I/O
- Network traffic
- Pod counts
- Container restarts

### Log Analytics

**Log Queries:**
```kusto
// Failed pods
ContainerLog
| where LogEntry contains "error" or LogEntry contains "failed"
| where Namespace == "kinana-dev"
| project TimeGenerated, ContainerName, LogEntry
| order by TimeGenerated desc

// High CPU containers
Perf
| where ObjectName == "K8SContainer"
| where CounterName == "cpuUsageNanoCores"
| summarize AvgCPU=avg(CounterValue) by Computer, InstanceName
| where AvgCPU > 800000000
```

---

## Backup and Disaster Recovery

### Backup Strategy

**AKS Cluster Configuration:**
- Infrastructure as Code (Git repository)
- Automated deployment pipelines
- Environment parity

**Persistent Data:**
```yaml
Azure Blob Storage:
  Method: Azure Storage snapshots
  Frequency: Daily at 02:00 UTC
  Retention: 30 days
  
MySQL Database:
  Method: mysqldump
  Frequency: Daily at 02:00 UTC
  Retention: 30 days
  Location: Azure Blob Storage
  
SQL Server:
  Method: Native SQL Server backups
  Frequency: Daily (full), Hourly (differential)
  Retention: 30 days (full), 7 days (differential)
```

### Disaster Recovery

**RTO/RPO:**
```yaml
Recovery Time Objective (RTO): 4 hours
Recovery Point Objective (RPO): 24 hours
Critical Systems RPO: 1 hour
```

**DR Procedures:**
1. Declare disaster
2. Spin up new AKS cluster
3. Restore persistent data from backups
4. Update DNS records
5. Verify functionality
6. Monitor closely

---

## Scaling

### Horizontal Pod Autoscaler (HPA)

**API Gateway HPA:**
```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: api-hpa
  namespace: kinana-dev
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: api
  minReplicas: 2
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
  - type: Resource
    resource:
      name: memory
      target:
        type: Utilization
        averageUtilization: 80
  behavior:
    scaleDown:
      stabilizationWindowSeconds: 300
      policies:
      - type: Percent
        value: 50
        periodSeconds: 60
```

### Cluster Autoscaler

**Configuration:**
```yaml
min-nodes: 3
max-nodes: 10
scale-down-enabled: true
scale-down-delay-after-add: 10m
scale-down-unneeded-time: 10m
```

---

## CI/CD Pipeline

### Azure DevOps

**Pipeline Stages:**
```yaml
1. Build:
   - Checkout code
   - Run tests
   - Build Docker image
   - Scan for vulnerabilities
   - Push to ACR

2. Deploy (Development):
   - Update Kubernetes manifests
   - Apply to kinana-dev namespace
   - Run smoke tests
   
3. Deploy (Production):
   - Manual approval
   - Blue/green deployment
   - Health checks
   - Rollback if needed
```

**Pipeline YAML:**
```yaml
trigger:
  branches:
    include:
    - main
    - develop

pool:
  vmImage: 'ubuntu-latest'

variables:
  - group: kinana-vars
  - name: imageRepository
    value: 'kinanaapi'
  - name: containerRegistry
    value: 'uepcr.azurecr.io'
  - name: tag
    value: '$(Build.BuildId)'

stages:
- stage: Build
  jobs:
  - job: BuildJob
    steps:
    - task: Docker@2
      inputs:
        containerRegistry: 'uepcr'
        repository: '$(imageRepository)'
        command: 'buildAndPush'
        Dockerfile: '**/Dockerfile'
        tags: |
          $(tag)
          latest

- stage: Deploy
  dependsOn: Build
  jobs:
  - deployment: DeployJob
    environment: 'kinana-dev'
    strategy:
      runOnce:
        deploy:
          steps:
          - task: Kubernetes@1
            inputs:
              connectionType: 'Kubernetes Service Connection'
              namespace: 'kinana-dev'
              command: 'apply'
              arguments: '-f manifests/'
```

---

## Cost Optimization

### Current Costs (Estimated Monthly)

| Resource | Estimated Cost |
|----------|----------------|
| AKS Cluster | $500 |
| Node Pools (VMs) | $800 |
| Azure Blob Storage | $200 |
| Azure Load Balancer | $50 |
| Azure Container Registry | $100 |
| Bandwidth (Egress) | $150 |
| **Total** | **$1,800** |

### Cost Optimization Strategies

1. **Right-sizing**
   - Monitor resource utilization
   - Adjust VM sizes based on actual usage
   - Use burstable VMs where appropriate

2. **Reserved Instances**
   - Purchase 1-year or 3-year reservations
   - Potential savings: 30-60%

3. **Storage Lifecycle**
   - Move aged data to Cool tier (after 30 days)
   - Move archived data to Archive tier (after 90 days)

4. **Spot Instances**
   - Use for non-critical workloads
   - Potential savings: up to 90%

---

## Operational Procedures

### Deployment

**Standard Deployment:**
```bash
# Update image tag
kubectl set image deployment/api \
  api=uepcr.azurecr.io/kinanaapi:1.0.1 \
  -n kinana-dev

# Monitor rollout
kubectl rollout status deployment/api -n kinana-dev
```

**Rollback:**
```bash
kubectl rollout undo deployment/api -n kinana-dev
```

### Scaling

**Manual Scaling:**
```bash
kubectl scale deployment api --replicas=5 -n kinana-dev
```

**Check HPA:**
```bash
kubectl get hpa -n kinana-dev
```

### Certificate Renewal

**Check Certificates:**
```bash
kubectl get certificates -n kinana-dev
```

**Force Renewal:**
```bash
kubectl delete secret kinana-api-secret -n kinana-dev
kubectl annotate certificate kinana-api \
  cert-manager.io/issue-temporary-certificate="true"
```

---

## Troubleshooting

### Common Issues

#### Pods Not Starting
```bash
# Check pod status
kubectl get pods -n kinana-dev

# Describe pod
kubectl describe pod <pod-name> -n kinana-dev

# Check logs
kubectl logs <pod-name> -n kinana-dev
```

#### Storage Issues
```bash
# Check PVCs
kubectl get pvc -n kinana-dev

# Check PV status
kubectl get pv

# Describe PVC
kubectl describe pvc kinana-files-dev -n kinana-dev
```

#### Network Issues
```bash
# Check services
kubectl get svc -n kinana-dev

# Check ingress
kubectl get ingress -n kinana-dev

# Test DNS
kubectl run -it --rm debug --image=busybox --restart=Never -- \
  nslookup api.kinana-dev.svc.cluster.local
```

---

**Document Version**: 1.0  
**Last Updated**: November 2024  
**Classification**: Unclassified
