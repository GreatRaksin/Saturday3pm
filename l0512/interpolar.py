#  index = low + [(val - lys[low]) * (high - low) / (lys[high] - lys[low])]

'''
index - вероятный индекс элемента

lys - массив ✅
val - искомое значение ✅
low - начальный индекс ✅
high - конечный индекс ✅

'''

array = [1, 4, 67, 899, 1023, 3444, 4453, 6778, 9000, 10111, 15555]
low = 0
high = len(array) - 1
val = int(input('Шо ищем? '))

while low <= high and array[low] <= val <= array[high]:  # val >= array[low] and val <= array[high]
    index = low + int(((float(high - low) / (array[high] - array[low])) * (val - array[low])))
    if array[index] == val:
        print(index)
        break
    if array[index] < val:
        low = index + 1
    else:
        high = index - 1