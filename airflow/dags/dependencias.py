from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime


def holaclase():
    print("Hola Clase de Intro a la Ingeniería de ml learning tarea 1")

with DAG(
    dag_id = "Dependencies_Operator",
    description = "Dag con varias dependencias",
    start_date = datetime(2023,10,31),
    schedule = "@once"
) as dag:
    t1 = PythonOperator(
        task_id="task_1",
        python_callable=holaclase
        )
    t2 = BashOperator(
        task_id="task_2",
        bash_command='echo "Hola Mundo en MLOps tarea 2"'
        ) 
    t3 = BashOperator(
        task_id="task_3",
        bash_command='echo "Hola Mundo en MLOps tarea 3"'
        )     
    t4 = BashOperator(
        task_id="task_4",
        bash_command='echo "Hola Mundo en MLOps tarea 4"'
        )         
    t1.set_downstream(t2)
    t2.set_downstream([t3, t4])