import sys
import os

# Add the root directory to PATH so part0 and part1 can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from part0.helper_functions import matrix_multiply

# Algorithm configuration
NORM_THRESHOLD = 1e-12


def qr_decomposition(A):
    """Phân tách ma trận A thành Q, R bằng Gram-Schmidt."""
    n = len(A)

    # Trích xuất các vector cột u_j
    u = []
    for j in range(n):
        col = []
        for i in range(n):
            col.append(A[i][j])
        u.append(col)

    q = [[0.0] * n for _ in range(n)]
    R = [[0.0] * n for _ in range(n)]

    for j in range(n):
        v = u[j]

        for i in range(j):
            dot_product = 0.0
            for k in range(n):
                dot_product += u[j][k] * q[i][k]
            R[i][j] = dot_product

            new_v = []
            for k in range(n):
                new_v.append(v[k] - R[i][j] * q[i][k])
            v = new_v

        norm_squared = 0.0
        for x in v:
            norm_squared += x * x
        R[j][j] = norm_squared ** 0.5

        if R[j][j] > NORM_THRESHOLD:
            for k in range(n):
                q[j][k] = v[k] / R[j][j]

    Q_final = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(q[j][i])
        Q_final.append(row)

    return Q_final, R


def get_eigenvalues(A, iterations=500):
    """Tính các trị riêng bằng thuật toán QR lặp."""
    A_k = []
    for row in A:
        A_k.append([float(x) for x in row])

    for _ in range(iterations):
        Q, R = qr_decomposition(A_k)
        A_k = matrix_multiply(R, Q)

    eigenvalues = []
    for i in range(len(A_k)):
        eigenvalues.append(round(A_k[i][i], 8))
    return eigenvalues
