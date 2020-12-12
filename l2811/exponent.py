from l2811.binary import binary

arr = [0, 1, 2, 5, 6, 12, 74, 81]


def Exponential(array, value):
    if array[0] == value:
        return 0
    index = 1
    while index < len(array) and array[index] <= value:
        index *= 2
    return binary(array[:min(index, len(array))], value)

