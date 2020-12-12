my_str = input('Введите строку: ')
empty_string = ''

for letter in range(len(my_str) - 1, -1, -1):
    empty_string += my_str[letter]

print(empty_string)

