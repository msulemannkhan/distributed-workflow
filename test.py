import requests
import json
import time


x = requests.get('http://localhost:8000/run_job')
if x.status_code == 200:
    response = json.loads(x.text)
    print(response)
job_id = response["job_id"]

# pending
isPending = True
tik = time.time()
while isPending:
    job_status_response = requests.get(
        'http://localhost:8000/job_status', 
        params={"job_id":job_id}
    )
    isPending = json.loads(job_status_response.text)["status"] == "pending"
    print("\rpending since ",  "%.2f" %(time.time() - tik), "seconds", end="")
print()
print(json.loads(job_status_response.text)["status"])
job_result_response = requests.get(
        'http://localhost:8000/job_result', 
        params={"job_id":job_id}
    )
print(json.loads(job_status_response.text))
if json.loads(job_status_response.text)["status"] == "success":
    print("\nJob Finished")
    print("Job result:",  json.loads(job_result_response.text))
else:
    print("\nJob status:", job_result_response.text)

