# Serial Matrix Addition

A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

rows = len(A)
cols = len(A[0])

C = [[0 for _ in range(cols)] for _ in range(rows)]

print("Serial Matrix Computation -->")

for i in range(rows):
    for j in range(cols):
        C[i][j] = A[i][j] + B[i][j]

print("Result Matrix:")
for row in C:
    print(row)