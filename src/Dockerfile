FROM python:3.12-alpine
ENV TZ "Europe/Moscow"
RUN apk update
RUN apk add postgresql-client mysql-client tzdata
RUN pip install APScheduler==3.10.4 boto3==1.34.33
ADD . .
CMD ["python3", "main.py"]
