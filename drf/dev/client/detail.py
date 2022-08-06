import requests
import json
endpoint = "http://localhost:8000/api/product/2/"

# endpoint = "https://httpbin.org/anything"

get_response = requests.get(endpoint)
get_response.raise_for_status()
x = get_response.json()
print(x)
