import requests
from flask import *
from flask_cors import CORS
from config import *


DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

if __name__ == "__main__":    
    app.run(debug=DEBUG)

@app.route("/", methods=["GET"])
def getRepos():
    try:
        username = request.args.get('username')
        url = f"https://api.github.com/users/{username}/repos"
        headers = {"Accept":"application/vnd.github.mercy-preview+json"}
        repos = requests.get(url, headers=headers, auth=(username, TOKEN)).json()
        projects = []
        for repo in repos:
            project = {
                "id": repo["id"],
                "name": repo["name"],
                "url": repo["html_url"],
                "description": repo["description"],
                "topics":repo["topics"],
                "language":repo["language"],
            }
            projects.append(project)
        return projects
    except Exception as e:
        return {"error": True, "message": str(e)}, 500