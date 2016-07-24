#Funcion que crea el issue con los datos proporcionados
import requests
from .github_token import g_token

def create_issue(titulo, body):
    org = "PythonGranada"
    repo = "organization"

    url = "https://api.github.com/repos/{}/{}/issues".format(org, repo)

    issue = {'title': titulo,
    'body': body,
    'labels': ["charlas"]}

    headers = {
    'Content-Type':'application/json',
    'Authorization': 'token %s' % g_token,
    }

    r=requests.post(url, headers=headers, json=issue);
    print(r.status_code,r.json())
