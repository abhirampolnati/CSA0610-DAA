def add(A, B):

    n = len(A)

    return [
        [A[i][j] + B[i][j] for j in range(n)]
        for i in range(n)
    ]


def subtract(A, B):

    n = len(A)

    return [
        [A[i][j] - B[i][j] for j in range(n)]
        for i in range(n)
    ]


def conventional_multiply(A, B):

    n = len(A)

    C = [[0 for j in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

    return C


def strassen(A, B):

    n = len(A)

    # Base case
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    mid = n // 2

    # Divide matrices into four parts
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]

    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    # Calculate seven products
    M1 = strassen(add(A11, A22), add(B11, B22))

    M2 = strassen(add(A21, A22), B11)

    M3 = strassen(A11, subtract(B12, B22))

    M4 = strassen(A22, subtract(B21, B11))

    M5 = strassen(add(A11, A12), B22)

    M6 = strassen(subtract(A21, A11), add(B11, B12))

    M7 = strassen(subtract(A12, A22), add(B21, B22))

    # Calculate result quadrants
    C11 = add(subtract(add(M1, M4), M5), M7)

    C12 = add(M3, M5)

    C21 = add(M2, M4)

    C22 = add(subtract(add(M1, M3), M2), M6)

    # Combine quadrants
    C = []

    for i in range(mid):
        C.append(C11[i] + C12[i])

    for i in range(mid):
        C.append(C21[i] + C22[i])

    return C


def strassen_multiply(A, B):

    n = len(A)

    size = 1

    while size < n:
        size *= 2

    # Pad matrices to the next power of 2
    P = [[0] * size for _ in range(size)]
    Q = [[0] * size for _ in range(size)]

    for i in range(n):
        for j in range(n):
            P[i][j] = A[i][j]
            Q[i][j] = B[i][j]

    result = strassen(P, Q)

    # Remove padding
    return [row[:n] for row in result[:n]]


A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

result = strassen_multiply(A, B)

print("Strassen Matrix Multiplication:")

for row in result:
    print(row)
