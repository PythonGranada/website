#Funcion que crea el issue con los datos proporcionados
import requests
import os

g_token = os.environ.get("GITHUB","")
def create_issue(titulo, body):
    #org = "PythonGranada"
    #repo = "organization"
    org = "yabirgb"
    repo = "website"

    url = "https://api.github.com/repos/{}/{}/issues?access_token={}".format(org, repo,g_token)

    issue = {'title': titulo,
    'body': body,
    'labels': ["charlas"]}

    headers = {
    'Content-Type':'application/json',
    }

    r=requests.post(url, headers=headers, json=issue);
    print(r.status_code,r.json())
