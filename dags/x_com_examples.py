from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
	'owner':'none',
	'retries':5,
	'retry_delay':timedelta(minutes=2)
}

    
def greet(age, ti):
    name = ti.xcom_pull(task_ids='name')
    print(f'hello, my name is {name}! I am {age} years old.')
    
def name():
    return "Maria"

with DAG(
	dag_id='xcom_xpull_example',
	default_args=default_args,
	description='', 
	start_date=datetime(2023, 3, 29),
	schedule_interval='@daily'
) as dag: 

    task1 = PythonOperator(
		task_id='greet', 
		python_callable=greet,
        op_kwargs={'age':20}
	)
    
    task2 = PythonOperator(
        task_id='name', 
        python_callable=name
    )
 
    task2 >> task1