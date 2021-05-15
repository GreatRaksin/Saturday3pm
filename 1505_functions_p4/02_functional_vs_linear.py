'''Есть список из чисел (все числа - str), необходимо создать новый список
и занести все значения из старого, трансформировав их в int'''

old_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
new_list = []
for item in old_list:
    new_list.append(int(item))
print(new_list)
print(type(new_list[1]))
# ^ линейный/процедурный код

nums = ['0', '1', '2', '3', '4', '5']
int_nums = list(map(int, nums))
print(int_nums)
# ^ функциональный


##############################################
def miles_to_km(num_miles):
    return num_miles * 1.6  # <- это не окей

distances = [1.4, 10.6, 8.4, 25.9, 2.3, 9]
km = list(map(lambda x: x * 1.6, distances))  # <- это окей
print(km)
