import json
import requests

url = 'http://localhost:3000/cars'
h = {'Content-Type': 'application/json'}

newcar = {
    'id': 9,
    'brand': 'Mazda',
    'model': '2 cd plusline',
    'production_year': '2007',
    'convertible': False,
}
try:
	reply = requests.post(url, headers=h, data=json.dumps(newcar))
except:
	print("A szerver nem elerheto")
	exit()
print(reply.status_code)
print(reply.text)
