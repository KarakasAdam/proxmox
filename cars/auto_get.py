import requests

try:
	reply=requests.get("http://localhost:3000/cars/2")
except:
	print("A szerver nem elerheto")
	exit()
print(reply.status_code)
print(reply.headers)
print(reply.text)
