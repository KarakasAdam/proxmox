import requests

reply=requests.get("http://localhost:3000/cars/2")
print(reply.status_code)
print(reply.headers)
print(reply.text)
