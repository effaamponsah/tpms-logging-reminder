import requests

url ='https://developerservice03.herokuapp.com/dev'

request_response = requests.get(url)

def getEmails():
    if request_response.status_code == 200:
        return request_response.text
    else:
        pass