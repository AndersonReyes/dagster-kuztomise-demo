FROM python:3.7-slim

ENV DAGSTER_HOME /opt/dagster/dagster_home

RUN apt-get update && apt-get install -yqq cron

RUN mkdir -p /opt/dagster/dagster_home /opt/dagster/app

RUN pip install dagit dagster dagster_cron dagster_postgres dagster_k8s dagster_slack

WORKDIR /opt/dagster/app

COPY pipelines .
COPY docker/entrypoint.sh entrypoint.sh

RUN chmod +x entrypoint.sh

EXPOSE 3000

ENTRYPOINT ["/opt/dagster/app/entrypoint.sh"]
