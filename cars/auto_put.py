import json
import requests
url = 'http://localhost:3000/cars/S2iQC73KM6w'
h = {'Content-Type': 'application/json'}
updated_car = {
    'brand': 'Porsche',
    'model': '911',
    'production_year': '1963',
    'convertible': False,
}
reply = requests.put(url, headers=h, data=json.dumps(updated_car))
print(reply.status_code)
print(reply.headers)
print(reply.text)
