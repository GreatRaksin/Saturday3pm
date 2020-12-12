from math import sqrt

s = int(input('что будем искать? '))
arr = [0, 1, 2, 5, 6, 12, 74, 81]

length = len(arr)
jump = int(sqrt(length))
left = 0
right = 0

while left < length and arr[left] <= s:
    right = min(length - 1, left + jump)
    if arr[left] <= s <= arr[right]:
        break
    left += jump
if left >= length or arr[left] > s:
    print(-1)
right = min(length - 1, right)
i = left
while i <= right and arr[i] <= s:
    if arr[i] == s:
        print(f'ID = {i}')
    i += 1