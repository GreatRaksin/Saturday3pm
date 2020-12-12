from random import randint

vedomost = []
students = int(input('Введите количество студентов: '))

for mark in range(students):
    vedomost.append(randint(4, 10))

print(vedomost)
good_mark = input('Какие оценки будем искать? ').split()
sum_of_good_marks = 0
sum_of_marks = 0

for string in range(len(good_mark)):
    good_mark[string] = int(good_mark[string])

for every_mark in vedomost:
    sum_of_marks += every_mark
    if every_mark in good_mark:
        # sum_of_good_marks = sum_of_good_marks + 1
        sum_of_good_marks += 1

print(f'Хороших оценок ({good_mark}): {sum_of_good_marks}.')
print(f'Среднее арифметическое: {sum_of_marks / len(vedomost)}.')
