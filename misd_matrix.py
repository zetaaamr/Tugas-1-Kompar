import numpy as np

def algo1(A, B):
    return A + B

def algo2(A, B):
    return np.add(A, B)

def algo3(A, B):
    return A.__add__(B)

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

r1 = algo1(A, B)
r2 = algo2(A, B)
r3 = algo3(A, B)

if (r1 == r2).all() or (r1 == r3).all():
    final = r1
elif (r2 == r3).all():
    final = r2
else:
    final = "ERROR"

print("MISD Result:")
print(final)