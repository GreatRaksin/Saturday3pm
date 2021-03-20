import json
# процесс кодирования JSON - сериализация

data = {
    'president': {
        'name': 'Richard Nixon',
        'age': 65,
    }
}

with open('data_json/data_file.json', 'w') as write_file:
    json.dump(data, write_file, indent=4)


