"""
This file contains the FastAPI application. It defines the routes for the API, 
which include a route to run the demo Prefect Flow, 
a route to get the status of a job, and a route to get the result of a job.
"""

from fastapi import FastAPI
from tasks import demo_celery_function

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/run_job")
def read_item():
    result = demo_celery_function.delay()
    return {
            'job_id': result.id,
            'status': result.status.lower()
        }

@app.get('/job_status')
def api_get_job_status(job_id: str):
    task = demo_celery_function.AsyncResult(job_id)
    response = {
            'status': task.status.lower(),
        }
    return response

@app.get('/job_result')
def api_get_job_graph(job_id):
    task = demo_celery_function.AsyncResult(job_id)
    return task.result