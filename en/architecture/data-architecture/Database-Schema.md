# Database Schema

## Overview

This document provides detailed schema information for all databases used in the Kinana Platform. The platform utilizes three primary database systems: Redis (caching), MySQL (file system metadata), and SQL Server (LTI integration).

## MySQL Database (FSDB) Schema

### Database Information

| Property | Value |
|----------|-------|
| Database Name | kinana_db |
| Version | MySQL 8.0 |
| Charset | utf8mb4 |
| Collation | utf8mb4_unicode_ci |
| Time Zone | UTC |

### Tables Overview

The FSDB contains the following main tables:

1. **files** - File metadata and properties
2. **folders** - Folder hierarchy and structure
3. **permissions** - Access control entries
4. **versions** - File version history
5. **users** - User information
6. **shares** - File sharing relationships
7. **tags** - File tagging system
8. **metadata** - Extended file attributes

---

### Table: `files`

**Purpose**: Stores metadata for all files in the system

```sql
CREATE TABLE `files` (
  `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `uuid` CHAR(36) NOT NULL UNIQUE,
  `name` VARCHAR(255) NOT NULL,
  `path` VARCHAR(2048) NOT NULL,
  `extension` VARCHAR(50),
  `mime_type` VARCHAR(100),
  `size` BIGINT UNSIGNED NOT NULL DEFAULT 0,
  `checksum` CHAR(64),
  `owner_id` BIGINT UNSIGNED NOT NULL,
  `folder_id` BIGINT UNSIGNED,
  `is_directory` BOOLEAN NOT NULL DEFAULT FALSE,
  `is_encrypted` BOOLEAN NOT NULL DEFAULT FALSE,
  `storage_provider` VARCHAR(50) NOT NULL DEFAULT 'azure_blob',
  `blob_container` VARCHAR(100),
  `blob_name` VARCHAR(500),
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `deleted_at` TIMESTAMP NULL,
  INDEX `idx_owner_id` (`owner_id`),
  INDEX `idx_folder_id` (`folder_id`),
  INDEX `idx_path` (`path`(255)),
  INDEX `idx_created_at` (`created_at`),
  INDEX `idx_deleted_at` (`deleted_at`),
  FULLTEXT INDEX `idx_name_fulltext` (`name`),
  FOREIGN KEY (`owner_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
  FOREIGN KEY (`folder_id`) REFERENCES `folders` (`id`) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

**Key Columns:**
- `uuid`: Globally unique identifier for external reference
- `path`: Full virtual path of the file
- `checksum`: SHA-256 hash for integrity verification
- `blob_name`: Azure Blob Storage identifier
- `deleted_at`: Soft delete timestamp

---

### Table: `folders`

**Purpose**: Manages folder hierarchy and structure

```sql
CREATE TABLE `folders` (
  `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `uuid` CHAR(36) NOT NULL UNIQUE,
  `name` VARCHAR(255) NOT NULL,
  `path` VARCHAR(2048) NOT NULL,
  `parent_id` BIGINT UNSIGNED,
  `owner_id` BIGINT UNSIGNED NOT NULL,
  `depth` INT UNSIGNED NOT NULL DEFAULT 0,
  `is_system` BOOLEAN NOT NULL DEFAULT FALSE,
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `deleted_at` TIMESTAMP NULL,
  INDEX `idx_parent_id` (`parent_id`),
  INDEX `idx_owner_id` (`owner_id`),
  INDEX `idx_path` (`path`(255)),
  INDEX `idx_deleted_at` (`deleted_at`),
  FOREIGN KEY (`parent_id`) REFERENCES `folders` (`id`) ON DELETE CASCADE,
  FOREIGN KEY (`owner_id`) REFERENCES `users` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

**Key Columns:**
- `parent_id`: Reference to parent folder (NULL for root)
- `depth`: Depth level in hierarchy (0 for root)
- `is_system`: Flag for system-managed folders

---

### Table: `permissions`

**Purpose**: Access control for files and folders

```sql
CREATE TABLE `permissions` (
  `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `resource_type` ENUM('file', 'folder') NOT NULL,
  `resource_id` BIGINT UNSIGNED NOT NULL,
  `user_id` BIGINT UNSIGNED,
  `group_id` BIGINT UNSIGNED,
  `permission_level` ENUM('read', 'write', 'admin') NOT NULL,
  `granted_by` BIGINT UNSIGNED NOT NULL,
  `granted_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `expires_at` TIMESTAMP NULL,
  INDEX `idx_resource` (`resource_type`, `resource_id`),
  INDEX `idx_user_id` (`user_id`),
  INDEX `idx_group_id` (`group_id`),
  INDEX `idx_expires_at` (`expires_at`),
  FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
  FOREIGN KEY (`granted_by`) REFERENCES `users` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

**Permission Levels:**
- `read`: View and download
- `write`: Read + upload, edit, delete
- `admin`: Write + grant permissions

---

### Table: `versions`

**Purpose**: Track file version history

```sql
CREATE TABLE `versions` (
  `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `file_id` BIGINT UNSIGNED NOT NULL,
  `version_number` INT UNSIGNED NOT NULL,
  `size` BIGINT UNSIGNED NOT NULL,
  `checksum` CHAR(64) NOT NULL,
  `blob_name` VARCHAR(500) NOT NULL,
  `comment` TEXT,
  `created_by` BIGINT UNSIGNED NOT NULL,
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  INDEX `idx_file_id` (`file_id`),
  INDEX `idx_version_number` (`file_id`, `version_number`),
  UNIQUE KEY `unique_file_version` (`file_id`, `version_number`),
  FOREIGN KEY (`file_id`) REFERENCES `files` (`id`) ON DELETE CASCADE,
  FOREIGN KEY (`created_by`) REFERENCES `users` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

**Key Features:**
- Sequential version numbering
- Immutable version records
- Links to historical blob storage

---

### Table: `users`

**Purpose**: User account information

```sql
CREATE TABLE `users` (
  `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `uuid` CHAR(36) NOT NULL UNIQUE,
  `email` VARCHAR(255) NOT NULL UNIQUE,
  `username` VARCHAR(100) NOT NULL UNIQUE,
  `display_name` VARCHAR(255),
  `tenant_id` BIGINT UNSIGNED,
  `storage_quota` BIGINT UNSIGNED NOT NULL DEFAULT 10737418240, -- 10GB
  `storage_used` BIGINT UNSIGNED NOT NULL DEFAULT 0,
  `is_active` BOOLEAN NOT NULL DEFAULT TRUE,
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  INDEX `idx_email` (`email`),
  INDEX `idx_tenant_id` (`tenant_id`),
  INDEX `idx_is_active` (`is_active`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

---

### Table: `shares`

**Purpose**: File sharing links and tokens

```sql
CREATE TABLE `shares` (
  `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `token` CHAR(64) NOT NULL UNIQUE,
  `file_id` BIGINT UNSIGNED NOT NULL,
  `created_by` BIGINT UNSIGNED NOT NULL,
  `password_hash` VARCHAR(255),
  `expires_at` TIMESTAMP NULL,
  `max_downloads` INT UNSIGNED,
  `download_count` INT UNSIGNED NOT NULL DEFAULT 0,
  `is_active` BOOLEAN NOT NULL DEFAULT TRUE,
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  INDEX `idx_token` (`token`),
  INDEX `idx_file_id` (`file_id`),
  INDEX `idx_expires_at` (`expires_at`),
  FOREIGN KEY (`file_id`) REFERENCES `files` (`id`) ON DELETE CASCADE,
  FOREIGN KEY (`created_by`) REFERENCES `users` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

---

### Table: `tags`

**Purpose**: File tagging system

```sql
CREATE TABLE `tags` (
  `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `name` VARCHAR(100) NOT NULL,
  `color` CHAR(7),
  `owner_id` BIGINT UNSIGNED NOT NULL,
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  UNIQUE KEY `unique_tag_owner` (`name`, `owner_id`),
  INDEX `idx_owner_id` (`owner_id`),
  FOREIGN KEY (`owner_id`) REFERENCES `users` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `file_tags` (
  `file_id` BIGINT UNSIGNED NOT NULL,
  `tag_id` BIGINT UNSIGNED NOT NULL,
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`file_id`, `tag_id`),
  FOREIGN KEY (`file_id`) REFERENCES `files` (`id`) ON DELETE CASCADE,
  FOREIGN KEY (`tag_id`) REFERENCES `tags` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

---

### Table: `metadata`

**Purpose**: Extended file attributes

```sql
CREATE TABLE `metadata` (
  `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `file_id` BIGINT UNSIGNED NOT NULL,
  `key` VARCHAR(100) NOT NULL,
  `value` TEXT,
  `value_type` ENUM('string', 'number', 'boolean', 'json') NOT NULL DEFAULT 'string',
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `unique_file_metadata` (`file_id`, `key`),
  FOREIGN KEY (`file_id`) REFERENCES `files` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

---

## SQL Server Database (LTI) Schema

### Database Information

| Property | Value |
|----------|-------|
| Database Name | lti_db |
| Server | 10.7.0.4:1433 |
| Version | SQL Server 2019 |
| Collation | SQL_Latin1_General_CP1_CI_AS |
| Prefix | kinana |

### Tables Overview

1. **kinana_tools** - LTI tool registrations
2. **kinana_platforms** - LMS platform configurations
3. **kinana_deployments** - Deployment instances
4. **kinana_launches** - Launch sessions
5. **kinana_grades** - Grade passback data
6. **kinana_resource_links** - Deep linking

---

### Table: `kinana_tools`

**Purpose**: LTI 1.3 tool registrations

```sql
CREATE TABLE kinana_tools (
    id INT IDENTITY(1,1) PRIMARY KEY,
    client_id NVARCHAR(255) NOT NULL UNIQUE,
    consumer_key NVARCHAR(255) NOT NULL,
    tool_url NVARCHAR(500) NOT NULL,
    public_key NVARCHAR(MAX),
    private_key NVARCHAR(MAX),
    scope NVARCHAR(255) NOT NULL DEFAULT 'openid',
    is_active BIT NOT NULL DEFAULT 1,
    created_at DATETIME2 NOT NULL DEFAULT GETUTCDATE(),
    updated_at DATETIME2 NOT NULL DEFAULT GETUTCDATE()
);
```

**Example Data:**
```sql
INSERT INTO kinana_tools (client_id, consumer_key, tool_url, scope)
VALUES 
    ('d84a22ff-7326-41f3-adce-5c9cb177e550', 'Akadimi', 
     'https://xwinji.app.kinana.ai', 'openid'),
    ('a2967543-a73f-4459-9b2a-6a3458bab2fe', 'Akadimi',
     'https://readerapp.app.kinana.ai', 'openid');
```

---

### Table: `kinana_platforms`

**Purpose**: LMS platform configurations

```sql
CREATE TABLE kinana_platforms (
    id INT IDENTITY(1,1) PRIMARY KEY,
    issuer NVARCHAR(500) NOT NULL UNIQUE,
    auth_endpoint NVARCHAR(500) NOT NULL,
    token_endpoint NVARCHAR(500) NOT NULL,
    jwks_endpoint NVARCHAR(500) NOT NULL,
    platform_name NVARCHAR(255),
    is_active BIT NOT NULL DEFAULT 1,
    created_at DATETIME2 NOT NULL DEFAULT GETUTCDATE(),
    updated_at DATETIME2 NOT NULL DEFAULT GETUTCDATE()
);
```

---

### Table: `kinana_launches`

**Purpose**: Track LTI launch sessions

```sql
CREATE TABLE kinana_launches (
    id INT IDENTITY(1,1) PRIMARY KEY,
    launch_id NVARCHAR(255) NOT NULL UNIQUE,
    tool_id INT NOT NULL,
    platform_id INT NOT NULL,
    user_id NVARCHAR(255),
    context_id NVARCHAR(255),
    resource_link_id NVARCHAR(255),
    launch_token NVARCHAR(MAX),
    state_token NVARCHAR(255),
    nonce NVARCHAR(255),
    launched_at DATETIME2 NOT NULL DEFAULT GETUTCDATE(),
    expires_at DATETIME2,
    FOREIGN KEY (tool_id) REFERENCES kinana_tools(id),
    FOREIGN KEY (platform_id) REFERENCES kinana_platforms(id)
);

CREATE INDEX idx_launch_id ON kinana_launches(launch_id);
CREATE INDEX idx_state_token ON kinana_launches(state_token);
CREATE INDEX idx_nonce ON kinana_launches(nonce);
```

---

### Table: `kinana_grades`

**Purpose**: Grade passback data

```sql
CREATE TABLE kinana_grades (
    id INT IDENTITY(1,1) PRIMARY KEY,
    launch_id NVARCHAR(255) NOT NULL,
    user_id NVARCHAR(255) NOT NULL,
    score DECIMAL(5,2),
    score_maximum DECIMAL(5,2),
    comment NVARCHAR(MAX),
    timestamp DATETIME2 NOT NULL DEFAULT GETUTCDATE(),
    status NVARCHAR(50) NOT NULL DEFAULT 'pending',
    FOREIGN KEY (launch_id) REFERENCES kinana_launches(launch_id)
);

CREATE INDEX idx_launch_user ON kinana_grades(launch_id, user_id);
```

---

## Redis Schema

### Key Patterns

Redis is used as a key-value store with the following patterns:

#### Session Storage
```
Pattern: session:{user_id}:{session_id}
Type: Hash
TTL: 3600 seconds (1 hour)
Fields:
  - user_id
  - email
  - roles
  - permissions
  - tenant_id
  - created_at
  - last_activity

Example:
session:12345:abc123xyz = {
  "user_id": "12345",
  "email": "user@example.com",
  "roles": ["student"],
  "tenant_id": "tenant_001"
}
```

#### API Response Cache
```
Pattern: api:response:{endpoint}:{params_hash}
Type: String (JSON)
TTL: 300 seconds (5 minutes)

Example:
api:response:files/list:7a3b9c = "[{...}, {...}]"
```

#### File Metadata Cache
```
Pattern: file:meta:{file_id}
Type: Hash
TTL: 3600 seconds (1 hour)

Example:
file:meta:uuid-here = {
  "name": "document.pdf",
  "size": "1048576",
  "mime_type": "application/pdf",
  "owner_id": "12345"
}
```

#### User Permissions Cache
```
Pattern: user:perms:{user_id}
Type: Set
TTL: 1800 seconds (30 minutes)

Example:
user:perms:12345 = ["read:files", "write:files", "admin:users"]
```

#### Rate Limiting
```
Pattern: ratelimit:{user_id}:{endpoint}
Type: String (counter)
TTL: 60 seconds (1 minute)

Example:
ratelimit:12345:upload = "5"
```

---

## Schema Maintenance

### Migration Strategy

**Version Control:**
- All schema changes tracked in Git
- Flyway or similar tool for migrations
- Rollback scripts for each migration

**Migration Process:**
1. Create migration script
2. Test in development environment
3. Review with team
4. Deploy to staging
5. Validate changes
6. Deploy to production
7. Monitor post-deployment

### Backup Procedures

**MySQL Backups:**
```bash
# Daily backup
mysqldump -u root -p kinana_db > backup_$(date +%Y%m%d).sql

# Compress
gzip backup_$(date +%Y%m%d).sql

# Upload to Azure Blob Storage
az storage blob upload \
  --container-name mysql-backups \
  --file backup_$(date +%Y%m%d).sql.gz
```

**SQL Server Backups:**
```sql
-- Full backup
BACKUP DATABASE lti_db 
TO DISK = 'C:\Backups\lti_db_full.bak'
WITH FORMAT, COMPRESSION;

-- Differential backup
BACKUP DATABASE lti_db 
TO DISK = 'C:\Backups\lti_db_diff.bak'
WITH DIFFERENTIAL, COMPRESSION;
```

### Performance Optimization

**MySQL Optimization:**
```sql
-- Analyze tables
ANALYZE TABLE files, folders, permissions;

-- Optimize tables
OPTIMIZE TABLE files, folders;

-- Update statistics
UPDATE TABLE files ANALYZE PARTITION ALL;
```

**Indexing Strategy:**
- Index foreign keys
- Index frequently queried columns
- Composite indexes for multi-column queries
- Full-text indexes for search fields

### Monitoring Queries

**MySQL Performance:**
```sql
-- Slow queries
SELECT * FROM mysql.slow_log 
WHERE query_time > 1
ORDER BY query_time DESC
LIMIT 10;

-- Table sizes
SELECT 
  table_name,
  ROUND(data_length / 1024 / 1024, 2) AS data_mb,
  ROUND(index_length / 1024 / 1024, 2) AS index_mb
FROM information_schema.tables
WHERE table_schema = 'kinana_db'
ORDER BY data_length DESC;
```

---

**Document Version**: 1.0  
**Last Updated**: November 2024  
**Classification**: Unclassified
