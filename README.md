# Fast Backup to S3 AWS

This project can help you to connect backup to everything by adding new service to docker compose file 

First of all you need to pass this parameters as ENV variables to your compose file

```
ENDPOINT_URL = (url of your s3)
BUCKET = 
SERVICE_NAME = (s3 or ec2, s3 is default)
AWS_SECRET_KEY = 
AWS_ACCESS_KEY = 

DB_HOST = 
DB_PORT = 
DB_NAME = 
DB_LOGIN = 
DB_PASSWORD = 
DB_TYPE = (mysql or postgres)

FILES = first/file/path;second/file/path;first/folder
BACKUP_INTERVAL = (in seconds)
```

