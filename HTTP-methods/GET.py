import requests


server = ""

body = {
    "email": "igrishkin77@gmail.com",
}

r = requests.get(server, json=body)
print(r.text)