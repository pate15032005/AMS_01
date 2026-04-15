
import os
import sys
import copy

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from part1.gaussian import gaussian_eliminate, back_substitution, forward_substitution
from part2.decomposition import cholesky
from part0.helper_functions import matrix_transpose

def gaussian_seidel(A, b, tol=1e-12, max_iter=1000, x0=None):
    """
    Giải hệ phương trình tuyến tính Ax = b bằng phương pháp Gauss-Seidel.
    A: Ma trận hệ số
    b: Vector hằng số
    x0: Nghiệm ban đầu (nếu None sẽ khởi tạo bằng vector 0)
    tol: Ngưỡng dừng dựa trên sai số tuyệt đối
    max_iter: Số lần lặp tối đa
    """
    n = len(A)
    x = x0 if x0 is not None else [0.0] * n
    last_error = float('inf')
    for iteration in range(max_iter):
        x_old = x[:]
        
        for i in range(n):
            if abs(A[i][i]) < 1e-12:
                raise ValueError("Zero diagonal element detected, Gauss-Seidel cannot proceed.")

            sum_ax = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x[i] = (b[i] - sum_ax) / A[i][i]
        
        # Kiểm tra điều kiện dừng
        error = max(abs(x[i] - x_old[i]) for i in range(n))
        if error < tol:
            # print(f"Converged in {iteration + 1} iterations.")
            return x
        
        if error > 1e15: # Nếu sai số quá lớn, có thể đang phân kỳ
            raise ValueError("Gauss-Seidel is diverging.")
        last_error = error

    return x

def solve_gaussian(A, b, use_fraction=False):
    return gaussian_eliminate(A, b, use_fraction=use_fraction)

def solve_cholesky(A, b):
    L = cholesky(A)
    # Giải Ly = b bằng thế xuôi
    y = forward_substitution(L, b)
    # Giải L^T x = y bằng thế ngược
    L_T = matrix_transpose(L)
    x = back_substitution(L_T, y)
    return x

# Hàm giải hệ phương trình tuyến tính bằng các phương pháp gauss-seidel
def solve_gauss_seidel(A, b, tol=1e-12, max_iterations=1000):
    return gaussian_seidel(A, b, tol, max_iterations)
