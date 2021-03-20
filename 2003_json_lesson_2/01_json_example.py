import json
import requests

url = 'https://jsonplaceholder.typicode.com/todos'
response = requests.get(url)
todos = json.loads(response.text)

with open('data_json/data_file.json', 'w') as write_file:
    json.dump(todos, write_file, indent=4)

todos_by_user = {}  # посчитаю работников, которые выполнили задачи
for todo in todos:
    if todo['completed']:
        try:
            # увеличить количество выполненных задач у пользователя
            todos_by_user[todo['userId']] += 1
        except KeyError:
            # если вдруг новый пользователь
            todos_by_user[todo['userId']] = 1
print(todos_by_user)

top = sorted(todos_by_user.items(),
             key=lambda x: x[1],
             # сортировать по количеству выполненных задач
             reverse=True)
print(top)
