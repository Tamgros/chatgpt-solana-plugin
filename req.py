import requests
import json


port = 3000
requests.get(f'http://localhost:{port}').text

j = json.dumps({"hello":"world"})
print(j)
print(type(j))

hey = requests.post(f'http://localhost:{port}/echo', json=json.loads(j)).text

print(hey)


# openapi_spec = requests.get(f'http://127.0.0.1:{port}/openapi.json').text

# print(openapi_spec)

# latest_blockhash = requests.get(f'http://127.0.0.1:{port}/get_latest_blockhash').text

# print(latest_blockhash)