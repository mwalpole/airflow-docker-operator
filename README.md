# Run Airflow with the Docker Operator

1. Start at the [apache-airflow project](https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html#before-you-begin)
2. Download the docker-compose template

```curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.1.2/docker-compose.yaml'```

3. Add an .env file for docker-compose to load the docker provider that has been fixed to enable access via remote endpoint

```_PIP_ADDITIONAL_REQUIREMENTS=apache-airflow-providers-docker==2.1.0rc1```

4. This is comparable to the following command which will install the providers on top of an existing airflow image
```
docker run -it -p 8080:8080 \
  --env "_PIP_ADDITIONAL_REQUIREMENTS=apache-airflow-providers-docker==1.1.0" \
  --env "_AIRFLOW_DB_UPGRADE=true" \
  --env "_AIRFLOW_WWW_USER_CREATE=true" \
  --env "_AIRFLOW_WWW_USER_PASSWORD_CMD=echo admin" \
    apache/airflow:2.1.2 webserver
```
5. For production we will build our own image explicitly rather than installing the providers anew every time we restart airflow
6. To run the example begin by initializing the airflow database
```
docker compose up airflow-init
```
7. Then run the full compose file
```
docker compose up -d
```
8. To tidy up run
```
docker compose down --rmi all --volumes
```