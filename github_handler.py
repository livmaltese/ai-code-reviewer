from github import Github
import os

g = Github(os.getenv("GITHUB_TOKEN"))

def get_pr_code(repo_name: str, pr_number: int) -> dict:
    repo = g.get_repo(repo_name)
    pull = repo.get_pull(pr_number)
    files = {}

    for file in pull.get_files():
        if file.status == "modified" and file.filename.endswith((".py", ".js", ".ts", ".java")):
            content = repo.get_contents(file.filename, ref=pull.head.ref)
            files[file.filename] = content.decoded_content.decode()

    return files
