def conventional_multiply(A, B):

    n = len(A)

    C = [[0 for j in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):

                C[i][j] += A[i][k] * B[k][j]

    return C


A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

result = conventional_multiply(A, B)

print("Conventional Matrix Multiplication:")

for row in result:
    print(row)
