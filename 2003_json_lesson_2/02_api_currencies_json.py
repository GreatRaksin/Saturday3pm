import requests
import json

url = 'https://api.coinbase.com/v2/currencies'
response = requests.get(url)
cur = json.loads(response.text)

with open('data_json/currency.json', 'w') as write_file:
    json.dump(cur, write_file, indent=4)

countries = {}
for c in cur['data']:
    countries[c['name']] = c['id']

with open('data_json/countries_codes.json', 'w') as wf:
    json.dump(countries, wf, indent=4)


