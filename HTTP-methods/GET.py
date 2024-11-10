import requests

server = ""

body = {
    "email": "igrishkin77@gmail.com",
    "PostIndex": " ",
    "Country": " ",
    "City": " ",
    "Street": " ",
    "Building": " ",
    "House": " ",
    "Apartment": " ",
    "AsDefault": " ",
    "CreatedAt": " ",
}

r = requests.get(server, json=body)
print(r.text)
