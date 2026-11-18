
import requests
url = 'http://localhost:3000/cars/kX0_plCzMaM'
reply = requests.delete(url)
print(reply.status_code)
print(reply.headers)
print(reply.text)
