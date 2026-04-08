import numpy as np

def rank_and_basis(A):
    m = len(A) # m dòng n cột 
    n = len(A[0])
    
    # tạo bản sao để dùng cho không gian cột 
    rref = [[float(val) for val in row] for row in A]
    
    pivot_row = 0
    pivot_cols = []

    # khử gauss logic giống inverse.py
    for j in range(n): 
        if pivot_row < m:
            max_idx = pivot_row
            for k in range(pivot_row + 1, m):
                if abs(rref[k][j]) > abs(rref[max_idx][j]):
                    max_idx = k
            
            # nếu cột toàn số 0 
            if abs(rref[max_idx][j]) < 1e-7:
                continue
            
            # hoán đổi dòng
            if max_idx != pivot_row:
                rref[pivot_row], rref[max_idx] = rref[max_idx], rref[pivot_row]
            
            # lưu lại chỉ số cột pivot để tính
            pivot_cols.append(j)

            # --- Đưa pivot về 1 ---
            pivot_val = rref[pivot_row][j]
            for k in range(n):
                rref[pivot_row][k] /= pivot_val
            
            # --- Khử các dòng khác về 0 ---
            for i in range(m):
                if i != pivot_row:
                    factor = rref[i][j]
                    for k in range(n):
                        rref[i][k] -= factor * rref[pivot_row][k]
                        if abs(rref[i][k]) < 1e-9: # Pate thêm đk này
                            rref[i][k] = 0.0 # để ép về 0, tránh tích lũy sai số   
            pivot_row += 1
    
    # 1. Hạng (Rank)
    rank = len(pivot_cols)
    
    # 2. Cơ sở không gian Dòng
    # lấy [rank] dòng của rref
    row_basis = [rref[i] for i in range(rank)]
    
    # 3. Cơ sở không gian Cột 
    column_basis = []
    for p_col in pivot_cols:
        col = [float(A[i][p_col]) for i in range(m)] # Lấy từng dòng của cột p_col
        column_basis.append(col)

    # 4. Cơ sở không gian Nghiệm
    null_basis = []
    free_vars = [c for c in range(n) if c not in pivot_cols] 
    
    for f_var in free_vars:
        special_sol = [0.0 for _ in range(n)]
        special_sol[f_var] = 1.0
        
        for r_idx, p_col in enumerate(pivot_cols): 
            special_sol[p_col] = -rref[r_idx][f_var]
        
        null_basis.append(special_sol)

    return rank, column_basis, row_basis, null_basis

def verify_rank_and_basis(A, my_rank):
    A_np = np.array(A, dtype=float)
    np_rank = np.linalg.matrix_rank(A_np)
    
    print(f"Calculated rank: {my_rank}")
    print(f"NumPy rank: {np_rank}")
    
    if my_rank == np_rank:
        print("RANK RESULT: CORRECT")
    else:
        print("RANK RESULT: INCORRECT")

if __name__ == "__main__":
    A_test = [[1, 2, 3], 
              [4, 5, 6], 
              [5, 7, 9]]
    
    print("Input matrix A:")
    for row in A_test:
        print(row)
    print("-" * 30)
    
    r, c_basis, r_basis, n_basis = rank_and_basis(A_test)
    
    print(f"Rank of matrix: {r}")
    
    print("\nBasis of Column Space:")
    for vec in c_basis: print([round(x, 4) for x in vec])
        
    print("\nBasis of Row Space:")
    for vec in r_basis: print([round(x, 4) for x in vec])
        
    print("\nBasis of Null Space:")
    if not n_basis:
        print("[] (Only solution x = 0)")
    else:
        for vec in n_basis: print([round(x, 4) for x in vec])
    print("-" * 30)
    
    verify_rank_and_basis(A_test, r)