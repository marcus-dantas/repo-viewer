import requests
from flask import *
# from flask_cors import CORS
from config import *
# from prettytable import PrettyTable

# table = PrettyTable()
# table.field_names = ["Repository Name", "Created Date"]

app = Flask(__name__)
# CORS(app)

if __name__ == "__main__":    
    app.run()

@app.route("/")
def welcome():
    return "<p>Github repo viewer</p>"

@app.route("/projects", methods=["GET"])
def getRepos():
    try:
        url = f"https://api.github.com/users/{USERNAME}/repos"
        headers = {"Accept":"application/vnd.github.mercy-preview+json"}
        repos = requests.get(url, headers=headers, auth=(USERNAME,TOKEN)).json()
        projects = []
        for repo in repos:
            # table.add_row([repo["name"], repo["created_at"]])
            # if repo["homepage"]:
            project = {
                "id": repo["id"],
                "name": repo["name"],
                "url": repo["html_url"],
                "description": repo["description"],
                "topics":repo["topics"],
                # "images": repo["homepage"].split(";")
            }
            projects.append(project)
        return {"projects": projects, "error": False}
        # print(table)
    except Exception as e:
        return {"error": True, "message": str(e)}, 500