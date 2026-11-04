import requests
api_endpoint = "https://meowfacts.herokuapp.com/?count=3"
response = requests.get(api_endpoint)
#for idx, fact in enumerate(response.json()["data"], start=1):
	#print(f"{idx}. {fact}")

print(response.headers)
#print(response.text)
