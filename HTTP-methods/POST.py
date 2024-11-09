import requests


server = ""

body = {
    "email": "igrishkin77@gmail.com",
}

r = requests.post(server, json=body)
print(r.text)