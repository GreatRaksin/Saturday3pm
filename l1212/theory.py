def my_isupper(letter):
    import string
    alph = string.ascii_uppercase
    return letter in alph


msg = input('Введите сообщение ')
sum = 0
for letter in msg:
    if letter.isupper():
        sum += 1
print(sum)