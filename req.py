import requests
import json
from solders.pubkey import Pubkey


port = 3333
requests.get(f'http://localhost:{port}').text

j = json.dumps({"hello":"world"})
# print(j)
# print(type(j))

# hey = requests.post(f'http://localhost:{port}/echo', json=json.loads(j)).text

# print(hey)

# latest_blockhash = requests.get(f'http://localhost:{port}/solana/get_latest_blockhash').text

# print(latest_blockhash)

pk = json.dumps({'pk': 'FNJhc44jGe9qPQVCWb9DEJrTGf7x2r3Yh2mpVEYhiGt7'})
len('2BDbYV1ocs2S1PsYnd5c5mqtdLWGf5VbCYvf28rs9LGj')
len('My11111111111111111111111111111111111111111')
# B1AfN7AgpMyctfFbjmvRAvE1yziZFDb9XCwydBjJwtRN
hey = requests.post(f'http://localhost:{port}/solana/get_account_info', json=json.loads(pk)).text

print(hey)


# openapi_spec = requests.get(f'http://127.0.0.1:{port}/openapi.json').text

# print(openapi_spec)

