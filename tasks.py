"""
This file contains the Celery tasks that are used to run the Prefect Flow. 
It also defines the Celery app and the Prefect agent.
"""
from celery import Celery
from prefect_tasks import github_stars

celery_app = Celery('tasks', backend='rpc://', broker='redis://backend_redis:6379//')



@celery_app.task
def demo_celery_function():
    print("demo_celery_function")
    repos = [
        "PrefectHQ/Prefect",
        "PrefectHQ/prefect-aws", 
        "PrefectHQ/prefect-dbt"
        ]
    # call the flow!
    print(repos)
    response = github_stars(repos)
    print(response)
    return repos