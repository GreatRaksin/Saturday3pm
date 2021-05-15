'''Функциональный код отличается тем, что у него отсутствуют побочные эффекты.
Он не полагается на данные вне функции и не меняет их.
'''

a = 0
def increment1():
    '''Вот это НЕ функциональный код'''
    global a
    a += 1


def increment2(a):
    '''А это функциональный'''
    return a + 1


nums = ['0', '1', '2', '3', '4', '5']
int_nums = map(int, nums)

for i in int_nums:
    print(type(i), end='')


s = map(lambda x: x * x, [1, 2, 3, 4, 5])
for i in s:
    print(i, end='⏰')
