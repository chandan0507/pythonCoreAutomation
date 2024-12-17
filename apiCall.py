import requests

def apiCallFrom(urlOfApi, variableName):
    headers = {'Content-Type': 'text/xml; charset=utf-8'}
    response = requests.request("POST", urlOfApi, headers=headers, data=variableName)
    return response.text