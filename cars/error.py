import requests
try:
	reply=requests.get("http://valami.hu")
except:
	print("A szerver nem elerheto!")
	exit()
print(reply.status_code)
print(reply.text)
