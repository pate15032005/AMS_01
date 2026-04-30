
import os
import sys
import copy
import numpy as np
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

# Hàm phụ trợ: Chuyển đổi nghiệm từ dạng 'list of dict' sang mảng NumPy 1D chuẩn
def clean_solution(x):
    """Đồng nhất kiểu trả về thành 1D numpy array float chuẩn"""
    if x is None:
        raise ValueError("Hệ vô nghiệm hoặc có lỗi trong quá trình giải.")
        
    # Xử lý kết quả từ back_substitution (List of Dicts)
    if isinstance(x, list) and len(x) > 0 and isinstance(x[0], dict):
        # Lấy đích danh giá trị 'const', bỏ qua các biến tự do (t_i) phát sinh do sai số
        clean_x = [float(item.get('const', 0.0)) for item in x]
        return np.array(clean_x, dtype=float)
    
    # Xử lý nếu đã là dict đơn lẻ
    if isinstance(x, dict):
        return np.array(list(x.values()), dtype=float)
        
    # Xử lý kết quả từ forward_substitution hoặc gauss_seidel (List of Floats)
    return np.array(x, dtype=float).flatten()


# 1. Sửa hàm Gaussian: Chỉ lấy phần tử thứ 1 (nghiệm x) và làm sạch
def solve_gaussian(A, b, use_fraction=False):
    # Ép kiểu an toàn từ numpy.ndarray sang list
    A_list = A.tolist() if isinstance(A, np.ndarray) else A
    b_list = b.tolist() if isinstance(b, np.ndarray) else b
    
    # Bóc tách rõ ràng tuple (A_work, x, swaps)
    A_work, x, swaps = gaussian_eliminate(A_list, b_list, use_fraction=use_fraction)
    return clean_solution(x)


# 2. Sửa hàm Cholesky: Chuyển đầu vào thành list chuẩn và làm sạch đầu ra
def solve_cholesky(A, b):
    A_list = A.tolist() if isinstance(A, np.ndarray) else A
    b_list = b.tolist() if isinstance(b, np.ndarray) else b
    
    L = cholesky(A_list)
    y = forward_substitution(L, b_list)
    L_T = matrix_transpose(L)
    x = back_substitution(L_T, y)
    
    return clean_solution(x)
# Hàm giải hệ phương trình tuyến tính bằng các phương pháp gauss-seidel
def solve_gauss_seidel(A, b, tol=1e-12, max_iterations=1000):
    A_list = A.tolist() if isinstance(A, np.ndarray) else A
    b_list = b.tolist() if isinstance(b, np.ndarray) else b
    
    x = gaussian_seidel(A_list, b_list, tol=tol, max_iter=max_iterations)
    return clean_solution(x)
