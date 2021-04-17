def describe_pet(name, type='hamster'):
    print(f'\nI have a {type}.')
    print(f'My {type} name is {name.title()}.')


describe_pet(name='lizzy', type='cat') # именованный аргумент

'''Допустимые вызовы функции'''
describe_pet('will')
describe_pet(name='will')

describe_pet('will', 'dog')
describe_pet(name='will', type='dog')
describe_pet(type='dog', name='will')

l = range(1, 10, 2)
print(l)