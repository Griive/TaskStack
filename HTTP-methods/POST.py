import requests

server = ""

body = {
    "email": "igrishkin77@gmail.com",
    "postIndex": " ",
    "country": " ",
    "city": " ",
    "street": " ",
    "building": " ",
    "house": " ",
    "apartment": " ",
    "asDefault": " ",
    "createdAt": " ",
}

r = requests.post(server, json=body)
print(r.text)
