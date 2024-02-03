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
DB_COLLECTION = (only for mongo)
DB_TYPE = (mysql or postgres or mongo)

FILES = first/file/path;second/file/path;first/folder
BACKUP_INTERVAL = (in seconds, backup every X secod from the moment of run)
SPECIFIC_TIME = 03:11 (if it is given the backup interval will be ignored)
```

The example of compose file you can see in `compose.yaml` file

What's important that you can only backup one the databases. For more databases create more services from the same image 

If you don't want to clone the project you can easily get the image from dockerhub [progerg/backup-s3](https://hub.docker.com/repository/docker/progerg/backup-s3). For correct working of the image please create also volumes to give one container to communicate with another

I recommend to mount to /home/backup

