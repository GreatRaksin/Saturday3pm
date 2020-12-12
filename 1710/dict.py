contacts = {
    'Mom': {
        'Phone': ['+375291234567', '+375297654321'],
        'Email': 'olga@icloud.com',
        'Date of Birth': '31/03/1968'
    },
    'Father': '+375331234567',
    'Cat': '+375251234567'
}

print(contacts['Mom']['Phone'][1])

contacts['Brother'] = '+375291009876' # добавление элемента
print(contacts)
contacts['Cat'] = '+375296665488' # замена элемента
print(contacts)

del contacts['Brother']
print(contacts)

for key, value in contacts.items():
    print(f'Key: {key},\n Value: {value}')