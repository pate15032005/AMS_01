from part1.gaussian import gaussian_eliminate, back_substitution
from part2.decomposition import cholesky
from part0.helper_functions import matrix_transpose

def forward_substitution(L, b):
    """
    Giải hệ phương trình tam giác dưới Ly = b bằng phép thế tiến (quét từ trên xuống)
    """
    n = len(b)
    y = [0.0] * n
    for i in range(n):
        sum_val = sum(L[i][j] * y[j] for j in range(i))
        y[i] = (b[i] - sum_val) / L[i][i]
    return y

def gaussian_seidel(A, b, x0=None, tol=1e-12, max_iter=1000):
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
    
    for iteration in range(max_iter):
        x_old = x.copy()
        
        for i in range(n):
            sum_ax = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x[i] = (b[i] - sum_ax) / A[i][i]
        
        # Kiểm tra điều kiện dừng
        error = max(abs(x[i] - x_old[i]) for i in range(n))
        if error < tol:
            # print(f"Converged in {iteration + 1} iterations.") tắt để benchmark
            break
            
    return x

# Phương pháp 1: Gauss 
def solve_gaussian(A, b):
    U, c, swaps = gaussian_eliminate(A, b) 
    x = back_substitution(U, c)
    return x

# Phương pháp 2: Cholesky 
def solve_cholesky(A, b):
    L = cholesky(A)
    
    # Giải Ly = b bằng THẾ TIẾN (forward) vì L là tam giác dưới
    y = forward_substitution(L, b)
    
    # Giải L^T x = y bằng THẾ NGƯỢC (back) vì L_T là tam giác trên
    L_T = matrix_transpose(L)
    x = back_substitution(L_T, y)
    
    return x

# Phương pháp 3: Gauss Seidel
def solve_gauss_seidel(A, b, tol=1e-10, max_iterations=1000):
    return gaussian_seidel(A, b, tol, max_iterations)