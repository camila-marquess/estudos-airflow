from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
	'owner':'none',
	'retries':5,
	'retry_delay':timedelta(minutes=2)
}

with DAG(
	dag_id='hello_world_catchup_parameter',
	default_args=default_args,
	description='testing airflow dag',
    start_date=datetime(2023, 4, 29),
	schedule_interval='@daily',
    catchup=True
) as dag:
    task1 = BashOperator(
	    task_id='first_task',
	    bash_command="echo hello, world!"
 )
    
task1