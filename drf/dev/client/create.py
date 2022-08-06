import requests
endpoint = "http://localhost:8000/api/product/"

# endpoint = "https://httpbin.org/anything"

get_response = requests.post(endpoint)
get_response.raise_for_status()
# x = get_response.json()
# print(x)
