from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
	'owner':'none',
	'retries':5,
	'retry_delay':timedelta(minutes=2)
}

with DAG(
	dag_id='hello_world_bash_operator',
	default_args=default_args,
	description='testing airflow dag', 
	start_date=datetime(2023, 3, 29),
	schedule_interval='@daily'
) as dag: 

	task1 = BashOperator(
		task_id='first_task',
		bash_command="echo hello, world!"
	)

	task2 = BashOperator(
			task_id='second_task',
			bash_command="echo hello, world!"
		)

	task3 = BashOperator(
			task_id='third_task',
			bash_command="echo hello, world!"
		)

task1.set_downstream(task2)
task1.set_downstream(task3)

#task1 >> [task2, task3]