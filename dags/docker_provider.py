from datetime import timedelta

from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago

import os, sys, json, logging
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

default_args = {
    'owner': 'john',
    'depends_on_past': False,
    'email': ['john@thehightable.org'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(minutes=15),
}

dag = DAG(
    'docker_operator_trigger_dag',
    default_args=default_args,
    schedule_interval=timedelta(days=1),
    start_date=days_ago(0),
)

t1 = DockerOperator(
    task_id='docker_operator_trigger_task',
    api_version='auto',
    # docker_url='tcp://localhost:2375',  # Set your docker URL
    network_mode='bridge',
    image='registry.gitlab.com/blogs-imsheth-com/airflow2-dockeroperator-nodejs-gitlab',
    auto_remove = True,
    force_pull = True,
    xcom_all = True,
    # tty = True, # turning this on screws up the log rendering
    # command = "", # use if required elsewhere
    environment={
        'ENVVAR1': "This is passed from DAG Task"
    },
    dag=dag,
)

t1

