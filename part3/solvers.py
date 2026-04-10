import numpy as np
from part1.gaussian import gaussian_eliminate, back_substitution
from part2.decomposition import cholesky

# Phương pháp 1: Giải bằng khử gauss
def solve_by_gauss(A, b):
    # Gọi hàm đã code ở Câu 1, Câu 2
    U, c, _ = gaussian_eliminate(A, b)
    x = back_substitution(U, c)
    return x

# Phương pháp 2: Giải bằng phân rã cholesky
def forward_substitution(L, b):
    """Hàm phụ: Giải hệ phương trình tam giác dưới Ly = b bằng thế tiến"""
    n = len(b)
    y = np.zeros(n)
    for i in range(n):
        sum_val = sum(L[i][j] * y[j] for j in range(i))
        y[i] = (b[i] - sum_val) / L[i][i]
    return y

def solve_by_decomposition(A, b):
    try:
        # Phân rã A thành L * L^T như ở decomposition.py
        L = cholesky(A)
    except ValueError as e:
        print(f"Lỗi: Không thể dùng Cholesky - {e}")
        return None
        
    # Giải Ly = b bằng thế tiến
    y = forward_substitution(L, b)
    
    # Giải L^T x = y bằng thế ngược
    L_T = np.transpose(L) 
    x = back_substitution(L_T, y) # Dùng lại hàm của gauss 
    
    return x

# Phương pháp 3: Lặp gauss - seidel
