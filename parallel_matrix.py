from multiprocessing import Process, Queue

def add_matrix_part(A, B, start, end, q):
    result = []
    for i in range(start, end):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] + B[i][j])
        result.append(row)
    q.put(result)

if __name__ == "__main__":

    A = [[1, 2],
         [3, 4]]

    B = [[5, 6],
         [7, 8]]

    q = Queue()

    p1 = Process(target=add_matrix_part, args=(A, B, 0, 1, q))
    p2 = Process(target=add_matrix_part, args=(A, B, 1, 2, q))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    result1 = q.get()
    result2 = q.get()

    final_result = result1 + result2

    print("Parallel Matrix Result:")
    for row in final_result:
        print(row)