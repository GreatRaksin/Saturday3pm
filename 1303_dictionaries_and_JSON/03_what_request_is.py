'''Словари по структуре похожи на
JSON ответы серверов. Науимся работать
с запросами и ответами.'''

import requests
# импортируем библиотеку для работы с запросами
'''Два вида запросов: GET и POST
Запросы класса GET позволяют получить
информацию от сервера.
'''
response = requests.get('https://api.github.com/')
'''<Response [200]> - Код ответа 2009
1xx - запрос получен, но процесс еще обрабатывается
2хх - успешное подключение
3хх - редирект. Запрос получен и перенаправлен в другое место
4xx - запрос содержит неверный синтаксис и не может быть обработан
5xx - свервер не может обработать !правильный! запрос
'''

# .status_code позволяет узнать код подключения
print(response.status_code)
if response:
    print('Пропускаем человека на сайт')
else:
    print('Генерируем страницу с ошибкой')

# .content позволяет получить содержимое ответа !в байтах!
print(response.content)
# .text позволяет получить содержимое ответа в виде текста
print(response.text)

with open('github.json', 'w') as f:
    f.write(str(response.json()))

url = 'https://api.github.com/users/greatraksin'

with open('gr.json', 'w') as n_f:
    n_f.write(str(requests.get(url).json()))

res = requests.get(url).json()
print('Подписчики у GR: ', res['followers'])

