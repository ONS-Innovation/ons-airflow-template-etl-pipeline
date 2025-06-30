import sys

sys.path.append("/Users/fahadanwar/genai-projects/etl-pipeline")  # Updated path

from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

from etl.extract import extract_data
from etl.load import load_data
from etl.transform import transform_data

default_args = {
    "owner": "airflow",
    "start_date": datetime(2023, 1, 1),
    "retries": 1,
}

with DAG(
    "etl_workflow",
    default_args=default_args,
    description="An ETL workflow that extracts, transforms, and loads data",
    schedule=None,
    catchup=False,
) as dag:

    def extract_task_callable(**kwargs):
        data = extract_data()
        return data

    def transform_task_callable(ti, **kwargs):
        data = ti.xcom_pull(task_ids="extract_data")
        transformed = transform_data(data)
        return transformed

    def load_task_callable(ti, **kwargs):
        data = ti.xcom_pull(task_ids="transform_data")
        load_data(data, "data/outputdata/output.csv")

    extract_task = PythonOperator(
        task_id="extract_data",
        python_callable=extract_task_callable,
    )

    transform_task = PythonOperator(
        task_id="transform_data",
        python_callable=transform_task_callable,
    )

    load_task = PythonOperator(
        task_id="load_data",
        python_callable=load_task_callable,
    )

    extract_task >> transform_task >> load_task
