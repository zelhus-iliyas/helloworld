import requests
import json
endpoint = "http://localhost:4200/"
endpoint = "http://localhost:8000/api/"

# endpoint = "https://httpbin.org/anything"

get_response = requests.post(endpoint,json={'message':'Hello World'})
get_response.raise_for_status()
x = get_response.json()
print(x)
