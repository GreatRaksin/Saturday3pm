def fizz_buzz(idx):
    if idx % 15 == 0:
        return 'fizz-buzz'  # Fizz-Buzz
    elif idx % 3 == 0:
        return 'fizz'  # Fizz
    elif idx % 5 == 0:
        return 'buzz'  # Buzz
    else:
        return str(idx)  # idX


for number in range(1, 16):
    print(fizz_buzz(number), end=' ')