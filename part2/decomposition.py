import numpy as np
import sys
import os

# Add the root directory to PATH to find 'part0'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from part0.helper_functions import print_matrix, matrix_transpose, matrix_multiply

def cholesky(A):
    n = len(A)

    # Khởi tạo ma trận L (tam giác dưới) với toàn giá trị 0
    L = [[0]*n for _ in range(n)]

    # Kiểm tra ma trận vuông
    for row in A:
        if len(row) != n:
            raise ValueError("Matrix is not square")

    # Kiểm tra ma trận đối xứng: A[i][j] = A[j][i]
    for i in range(n):
        for j in range(i+1, n):
            # So sánh A[i][j] và A[j][i] với một ngưỡng nhỏ để tránh lỗi do số thực
            if abs(A[i][j] - A[j][i]) > 1e-9:
                raise ValueError("Matrix is not symmetric")
    
    # Thực hiện phân rã Cholesky: A = L * L^T
    for j in range(n):
        # Tính phần tử đường chéo L[j][j]
        sum_diag = 0
        for k in range(j):
            sum_diag += L[j][k] ** 2

        value = A[j][j] - sum_diag
        if value <= 0:
            raise ValueError("Matrix is not positive definite")

        L[j][j] = value ** 0.5

         # Tính các phần tử dưới đường chéo trong cột j
        for i in range(j+1, n):
            sum_sub = 0
            for k in range(j):
                sum_sub += L[i][k] * L[j][k]

            L[i][j] = (A[i][j] - sum_sub) / L[j][j]

    return L


def verify_with_numpy(A, L):
    # chuyển sang numpy array
    A_np = np.array(A)
    L_np = np.array(L)

    # tính lại A từ L * L^T
    A_reconstructed = L_np @ L_np.T

    # so sánh gần đúng (do sai số số thực)
    if np.allclose(A_np, A_reconstructed):
        return True
    else:
        return False

def test_cholesky():
    # Danh sách các test case:
    # - Ma trận hợp lệ (SPD)
    # - Ma trận không đối xứng
    # - Ma trận không xác định dương
    # - Ma trận không vuông
    test_cases = [
        ("Valid 2x2", [[4,2],[2,3]]),
        ("Valid 3x3", [[25,15,-5],[15,18,0],[-5,0,11]]),
        ("Not symmetric", [[1,2],[3,4]]),
        ("Not positive definite", [[1,2],[2,1]]),
        ("Not square", [[1,2,3],[4,5,6]])
    ]

    for name, A in test_cases:
        print("\n- Test: {}".format(name))

        # in ma trận A
        print_matrix("Matrix A", A)

        try:
            L = cholesky(A)

            print_matrix("L (Cholesky factor)", L)

            is_correct = verify_with_numpy(A, L)
            print("Verify with NumPy:", is_correct)
        except Exception as e:
            print("Error:", e)

test_cholesky()