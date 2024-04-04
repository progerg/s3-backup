FROM python:3.12-alpine
ENV TZ "Europe/Moscow"
RUN mkdir "/home/backup"
WORKDIR "/home/backup"
RUN apk update
RUN apk add postgresql-client mysql-client tzdata mongodb-tools
RUN pip install APScheduler==3.10.4 boto3==1.34.33 requests==2.31.0
ADD . .
CMD ["python3", "main.py"]
