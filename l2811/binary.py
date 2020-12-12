
def binary(arr, val):
    first = 0
    last = len(arr) - 1
    mid = len(arr) // 2
    while first <= last and arr[mid] != val:
        if val > arr[mid]:
            first = mid + 1
        else:
            last = mid - 1

        mid = (last + first) // 2
    return mid
