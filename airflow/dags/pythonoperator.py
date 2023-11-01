from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def holaclase():
    print("Hola Clase de Intro a la Ingeniería de ml learning")

with DAG(
    dag_id = "Python_Operator",
    description = "Primer DAG Python Operator para clase MLOps",
    start_date = datetime(2023,10,31),
    schedule = "@once"
) as dag:
    t1 = PythonOperator(
        task_id="python_saludo",
        python_callable=holaclase
        )
    t1