import requests

response = requests.get('http://localhost:8000/index.html')

print("Response Headers:")

for key, value in response.headers.items():
    print(f"{key}: {value}")

print("\n Response Body:")
print(response.text)