from airflow import DAG
from airflow.operators.empty import EmptyOperator
from datetime import datetime

with DAG(
    dag_id = "primer_dag",
    description = "Primer DAG para clase MLOps",
    start_date = datetime(2023,10,28),
    schedule = "@once"
) as dag:
    t1 = EmptyOperator(task_id="Dummy_1")
    t1