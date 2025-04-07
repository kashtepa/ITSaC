import requests
import json

def postHttpbin():
    url = "https://httpbin.org/post?name=qwerty&abc=1232222222222222"

    payload = json.dumps({
      "lmane": "qwrtyiop",
      "id": 123,
      "isActive": True
    })
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    return response

if __name__ == '__main__':
    postHttpbin()