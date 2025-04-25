from fastapi import FastAPI, Request
from github_handler import get_pr_code
from llm_reviewer import review_code
import os
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "AI Reviewer running"}

@app.post("/review")
async def review_pull_request(request: Request):
    data = await request.json()
    repo_name = data["repo"]
    pr_number = data["pr"]

    files = get_pr_code(repo_name, pr_number)
    reviews = []

    for filename, code in files.items():
        feedback = review_code(code)
        reviews.append({
            "file": filename,
            "review": feedback
        })

    return {"reviews": reviews}
