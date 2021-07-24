from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.docker_operator import DockerOperator
from airflow.operators.dummy_operator import DummyOperator

default_args = {
'owner'                 : 'airflow',
'description'           : 'Use of the DockerOperator',
'depend_on_past'        : False,
'start_date'            : datetime(2021, 5, 1),
'email_on_failure'      : False,
'email_on_retry'        : False,
'retries'               : 0,
# 'retry_delay'           : timedelta(minutes=5)
}

with DAG('docker_operator_dag', default_args=default_args, schedule_interval="5 * * * *", catchup=False) as dag:
    start_dag = DummyOperator(
        task_id='start_dag'
        )

    end_dag = DummyOperator(
        task_id='end_dag'
        )        

    t1 = DockerOperator(
        task_id='docker_command_sleep',
        image='centos:latest',
        # container_name='task___command_sleep',
        api_version='auto',
        auto_remove=True,
        command="/bin/sleep 30",
        docker_url='tcp://docker-proxy:2375',
        # docker_url="unix://var/run/docker.sock",
        network_mode="bridge",
        mount_tmp_dir=False
        )

start_dag >> t1 >> end_dag