"""
Vì đồ án yêu cầu phải cài đặt tất cả các hàm từ đầu, 
nên nhóm đã viết lại một số hàm tiện ích trong file này để sử dụng chung cho phần sau.
"""
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from part1.determinant import determinant

def print_matrix(title, M):
    """    In ma trận với tiêu đề và định dạng đẹp.    """
    print("\n{}:".format(title))
    for row in M:
        row_str = ""
        for val in row:
            row_str += "  {:10.4f}".format(val)
        print(row_str)

def create_identity(n):
    """    Tạo ma trận đơn vị bậc n.    """
    return [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]

def matrix_multiply(A, B):
    """    Nhân hai ma trận A và B.    """
    if len(A[0]) != len(B):
        raise ValueError("Matrix dimensions do not match for multiplication")
    m, n, p = len(A), len(A[0]), len(B[0])
    res = [[0.0 for _ in range(p)] for _ in range(m)]
    for i in range(m):
        for j in range(p):
            for k in range(n):
                res[i][j] += A[i][k] * B[k][j]
    return res

def matrix_subtract(A, B):
    """    Trừ hai ma trận A và B.    """
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Matrix dimensions do not match for subtraction")
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] - B[i][j])
        result.append(row)
    return result

def get_trace(A):
    """    Tính trace của ma trận A (tổng các phần tử trên đường chéo chính).    """
    if len(A) != len(A[0]):
        raise ValueError("Matrix must be square to calculate trace")
    return sum(A[i][i] for i in range(len(A)))

def matrix_transpose(A):
    """    Trả về ma trận chuyển vị của A.    """
    n = len(A)
    m = len(A[0])
    # Khởi tạo ma trận chuyển vị T có kích thước m x n
    T = [[0]*n for _ in range(m)]
    # Duyệt qua từng phần tử của A
    for i in range(n):
        for j in range(m):
            # Hoán đổi vị trí: phần tử A[i][j] -> T[j][i]
            T[j][i] = A[i][j]
    return T


def verify_matrix_invertible(P):
    """Kiểm tra ma trận P có khả nghịch hay không bằng cách tính định thức."""
    try:
        # Import determinant locally to avoid circular imports
        det_p = determinant(P)
        if abs(det_p) < 1e-9:
            return False, "Matrix P is singular (not invertible)."
        return True, "Valid"
    except Exception as e:
        return False, "Error computing determinant: {}".format(e)
