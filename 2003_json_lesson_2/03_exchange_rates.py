import requests
import json

f_cur = 'EUR'  # евро
t_cur = 'USD'  # доллар

url = f'https://api.coinbase.com/v2/exchange-rates?currency={f_cur}'
response = requests.get(url)
cur = json.loads(response.text)  # ответ сервера в json туть

print(cur['data']['rates'][t_cur])