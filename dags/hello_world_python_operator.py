from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
	'owner':'none',
	'retries':5,
	'retry_delay':timedelta(minutes=2)
}

def greet():
    print('hello, world!')
    
def greet_name_age(name, age):
    print(f'hello, my name is {name}! I am {age} years old.')

with DAG(
	dag_id='greet_in_python_operator',
	default_args=default_args,
	description='', 
	start_date=datetime(2023, 3, 29),
	schedule_interval='@daily'
) as dag: 

	task1 = PythonOperator(
		task_id='first_task',
		python_callable=greet
	)
 
	task2 = PythonOperator(
		task_id='second_task',
		python_callable=greet_name_age,
        op_kwargs={'name':'Maria', 'age':20} 
	)
 
task1
task2