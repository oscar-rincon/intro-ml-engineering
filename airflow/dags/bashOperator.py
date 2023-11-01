from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime


with DAG(
    dag_id = "Bash_Operator",
    description = "Primer DAG Bash Operator para clase MLOps",
    start_date = datetime(2023,10,31),
    schedule = "@once"
) as dag:
    t1 = BashOperator(
        task_id="hola_clase",
        bash_command='echo "Hola Mundo en MLOps"')
    t1