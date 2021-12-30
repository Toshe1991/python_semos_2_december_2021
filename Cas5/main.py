import requests

# response = requests.get('https://api.ipify.org?format=json')
#
# print(response.content["ip"])
#
# print(response.json()["ip"])

# # print(response.content)
#
# print(response.headers)

response = requests.get("http://127.0.0.1:5000/json")

response = response.json()
print(type(response))
print(response)