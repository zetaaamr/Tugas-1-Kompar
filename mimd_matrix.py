from multiprocessing import Process

def square_matrix(A):
    print("Square Matrix:")
    print(A * A)

def add_matrix(A, B):
    print("\nAdd Matrix:")
    print(A + B)

if __name__ == "__main__":
    import numpy as np

    A = np.array([[1, 2],
                  [3, 4]])

    B = np.array([[5, 6],
                  [7, 8]])

    p1 = Process(target=square_matrix, args=(A,))
    p2 = Process(target=add_matrix, args=(A, B))

    p1.start()
    p2.start()

    p1.join()
    p2.join()