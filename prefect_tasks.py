"""
This file contains an example of a Prefect Flow that uses the get_stars Task to 
get the number of stars for a given GitHub repository. The Flow receives a 
list of repository names and returns a dictionary of repository names and 
the number of stars they have.
"""

from prefect import flow, task
import httpx

@task(retries=3)
def get_stars(repo):
    return f"{repo} has {len(repo)} stars!"

@flow
def github_stars(repos):
    responses = {}
    for repo in repos:
        responses[repo] = get_stars(repo)
    return responses

if __name__ == "__main__":
    repos = [
        "PrefectHQ/Prefect",
        "PrefectHQ/prefect-aws", 
        "PrefectHQ/prefect-dbt"
    ]
    response = github_stars(repos)
    print(response)