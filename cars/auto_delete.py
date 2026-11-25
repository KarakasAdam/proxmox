
import requests
url = 'http://localhost:3000/cars/kX0_plCzMaM'
try:
	reply = requests.delete(url)
except:
	print("A szerver nem elerheto")
	exit()
print(reply.status_code)
print(reply.headers)
print(reply.text)
