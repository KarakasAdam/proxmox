import json
import requests
url = 'http://localhost:3000/cars/S2iQC73KM6w'
h = {'Content-Type': 'application/json'}
updated_car = {
    'brand': 'Mazda',
    'model': '2',
    'production_year': '2007',
    'convertible': False,
}
reply = requests.put(url, headers=h, data=json.dumps(updated_car))
print(reply.status_code)
print(reply.headers)
print(reply.text)
