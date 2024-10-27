import requests

result = requests.get("http://127.0.0.1:5000/")
print("base result print put ===", result)
result_json = result.json()
print(result_json)

