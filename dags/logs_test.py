from airflow.decorators import dag, task
from airflow.utils.dates import days_ago
from datetime import timedelta
import logging

# Define default arguments
default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

# Define the DAG
@dag(
    default_args=default_args,
    description='A simple example DAG to demonstrate logging',
    schedule_interval=None,
    start_date=days_ago(1),
    tags=['example', 'logging']
)
def example_logging_dag():

    @task
    def start_task():
        logger = logging.getLogger("airflow.task")
        logger.info("Starting the example DAG with logging!")
        return "Start"

    @task
    def process_task(start_message: str):
        logger = logging.getLogger("airflow.task")
        logger.info(f"Processing the message: {start_message}")
        for i in range(5):
            logger.info(f"Process step {i+1}/5 complete.")
        return "Process Complete"

    @task
    def end_task(process_message: str):
        logger = logging.getLogger("airflow.task")
        logger.info(f"Ending the example DAG with message: {process_message}")

    # Task dependencies
    start_msg = start_task()
    process_msg = process_task(start_msg)
    end_task(process_msg)

# Instantiate the DAG
example_logging_dag_instance = example_logging_dag()
