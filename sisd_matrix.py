# SISD Matrix Addition

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

C = []

for i in range(len(A)):
    row = []
    for j in range(len(A[0])):
        row.append(A[i][j] + B[i][j])
    C.append(row)

print("SISD Result:", C)