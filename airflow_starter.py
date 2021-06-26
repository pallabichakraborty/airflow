# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from datetime import timedelta
from textwrap import dedent

from airflow import DAG

from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['pallavichakraborty@yahoo.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(days=1)
}


def show_me_what_you_can_do():
    print("I dont know Airflow")


with DAG(
        'python_airflow',
        default_args=default_args,
        description='Python DAG',
        schedule_interval=timedelta(days=1),
        start_date=days_ago(2),
        tags=['example'],
) as dag:
    run_etl = PythonOperator(
        task_id='something',
        python_callable=show_me_what_you_can_do
    )
    run_etl.doc_md = dedent(
        """\
    #### Some comment"""
    )

run_etl