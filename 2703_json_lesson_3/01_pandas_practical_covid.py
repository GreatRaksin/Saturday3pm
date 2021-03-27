import pandas as pd
import json
import requests
import matplotlib.pyplot as plt  # импорт библиотеки с диаграммами

url = 'https://api.statworx.com/covid'
payload = {'country': 'France'}  #
response = requests.post(url, data=json.dumps(payload))
# https://api.statworx.com/covid?country=Russia|code=RU

with open('covid.json', 'w') as f:
    json.dump(json.loads(response.text), f, indent=4)
    # загрузить в файл( загрузить(ответ сервера), в файл)

df = pd.DataFrame.from_dict(json.loads(response.text))
print(df[df.cases > 1000][['cases', 'deaths']])

df.plot(x='date', y=['cases', 'deaths'], rot=10, fontsize=8)
plt.show()

top_5 = df.sort_values(by='deaths', ascending=False).head(3)
top_5.plot(x='date', y='deaths', kind='bar', rot=15, fontsize=4)
plt.show()

df.plot(x='date', y=['cases', 'population'], rot=10, fontsize=8)
plt.show()
