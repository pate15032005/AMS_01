import numpy as np
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from part0.helper_functions import print_matrix
from part1.determinant import determinant

def inverse(A):
    # kiểm tra định thức
    det_A = determinant(A)
    if abs(det_A) < 1e-12:
        raise ValueError("Matrix is not invertible because determinant is 0.")
    n = len(A)
    
    # tạo ma trận ghép
    combined = []
    for i in range(n): #dòng i cột j
        row = []
        # ma trận A
        for j in range(n):
            row.append(float(A[i][j]))
        # ma trận đơn vị I
        for j in range(n):
            if i == j:
                row.append(1.0)
            else:
                row.append(0.0)
        combined.append(row)
    
    # Biến đổi sơ cấp 
    for i in range(n):
        # tìm dòng chứa số lớn nhất trong cột
        max_row = i
        max_val = abs(combined[i][i])
        for k in range(i + 1, n):
            if abs(combined[k][i]) > max_val:
                max_val = abs(combined[k][i])
                max_row = k
                
        # hoán đổi 2 dòng
        if max_row != i:
            combined[i], combined[max_row] = combined[max_row], combined[i]

        # đưa pivot về 1
        pivot = combined[i][i] 
        for k in range(2 * n): # 2*n vì là ma trận ghép 
            combined[i][k] /= pivot 
            
        # khử về dòng 0
        for j in range(n):
            if i != j:
                factor = combined[j][i]
                for k in range(2 * n):
                    combined[j][k] -= factor * combined[i][k]
    
    # tách kết quả A^-1
    A_inv = []
    for i in range(n):
        row = []
        for j in range(n, 2 * n): # cắt lấy nửa phải
            row.append(combined[i][j])
        A_inv.append(row)
        
    return A_inv 

def verify_solution(A, A_inv):
    A_np = np.array(A, dtype=float)
    A_inv_np = np.array(A_inv, dtype=float) # tạo 2 ma trận numpy
    n = A_np.shape[0]
    
    identity_check = np.dot(A_np, A_inv_np) # nhân 2 ma trận
    I = np.eye(n)
    
    is_identity = np.allclose(identity_check, I, atol=1e-8)
    
    try:
        np_inv = np.linalg.inv(A_np)
        is_correct_with_numpy = np.allclose(A_inv_np, np_inv, atol=1e-8)
    except np.linalg.LinAlgError:
        is_correct_with_numpy = False 
        
    print(f"1. A * A_inv = I: {'CORRECT' if is_identity else 'INCORRECT'}")
    print(f"2. Matches NumPy: {'CORRECT' if is_correct_with_numpy else 'INCORRECT'}")
    
    return is_identity and is_correct_with_numpy

if __name__ == "__main__":
    A_test = [[0, 2, 1], 
              [1, -1, 1], 
              [2, 4, 2]]

    try:
        my_inv = inverse(A_test) 
        print("Calculated inverse matrix:")
        for row in my_inv:
            print([round(x, 4) for x in row]) 
        
        print("\nVERIFICATION")
        verify_solution(A_test, my_inv)
    except Exception as e:
        print(f"Error: {e}")