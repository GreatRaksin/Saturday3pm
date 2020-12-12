#A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
#B = [1, 2, 3, 4, 5, 6]

#print(B[2])
#print(A[0][2])
A = []
m = 5
for i in range(5):
    A.append([0] * m)

for i in range(len(A)):
    for j in range(len(A[i])):
        print(A[i][j], end=' ')
    print()