'''Task 1.
Создать файл, закидать его числами через пробел
Написать программу, которая посчитает и выведем сумму всех чисел, которые хранятся в файле.

nums.txt <- 5 6 2 4
-> 17
'''

file = open('nums.txt')  # открою файл
readed = file.read()  # прочитать все из файла
array_of_numbers = readed.split()

for number in range(len(array_of_numbers)):
    array_of_numbers[number] = int(array_of_numbers[number])

print(sum(array_of_numbers))