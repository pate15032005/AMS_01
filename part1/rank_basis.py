import numpy as np

def rank_and_basis(A):
    matrix = np.array(A, dtype=float)
    m, n = matrix.shape
    
    rref = matrix.copy()
    
    pivot_row = 0
    pivot_cols = []

    # khu gauss logic giong inverse.py
    for j in range(n): 
        if pivot_row < m:
            max_idx = pivot_row + np.argmax(np.abs(rref[pivot_row:, j])) 
            if np.abs(rref[max_idx, j]) < 1e-12: #truong hop cot ko co pivot (toan so 0)
                continue
            
            rref[[pivot_row, max_idx]] = rref[[max_idx, pivot_row]]
            
            # luu lai chi so cot pivot de xac dinh co so sau nay 
            pivot_cols.append(j)

            pivot_val = rref[pivot_row, j]
            rref[pivot_row] = rref[pivot_row] / pivot_val
            
            for i in range(m):
                if i != pivot_row:
                    factor = rref[i, j]
                    rref[i] = rref[i] - factor * rref[pivot_row]
            
            pivot_row += 1

    # tinh toan cac yeu cau
    # hang (Rank) = so luong cot pivot tim duoc 
    rank = len(pivot_cols)
    
    # co so khong gian Dong R(A): Cac dong khac 0 trong RREF 
    row_basis = rref[:rank]
    
    # co so khong gian Cot C(A): Cac cot tuong ung pivot lay tu ma tran GOC 
    column_basis = matrix[:, pivot_cols].T 

    # co so khong gian Nghiem N(A): Giai Ax = 0 tu RREF 
    null_basis = []
    free_vars = [c for c in range(n) if c not in pivot_cols] 
    
    for f_var in free_vars:
        special_sol = np.zeros(n)
        special_sol[f_var] = 1 # Dat mot bien tu do = 1 (so nao khac cung duoc)
        for r_idx, p_col in enumerate(pivot_cols): #r_idx la so dong, p_col la cot pivot
            special_sol[p_col] = -rref[r_idx, f_var]
        null_basis.append(special_sol)

    return rank, column_basis, row_basis, np.array(null_basis)

def verify_rank_and_basis(A, my_rank):
    A_np = np.array(A)
    np_rank = np.linalg.matrix_rank(A_np)
    
    print(f"Rank tu tinh: {my_rank}")
    print(f"Rank cua NumPy: {np_rank}")
    
    if my_rank == np_rank:
        print("=> KET QUA RANK: CHINH XAC")
    else:
        print("=> KET QUA RANK: SAI")

if __name__ == "__main__":
    A_test = [[1, 2, 3], 
              [4, 5, 6], 
              [5, 7, 9]]
    
    print("Ma tran dau vao A:")
    print(np.array(A_test))
    print("-" * 30)
    
    r, c_basis, r_basis, n_basis = rank_and_basis(A_test)
    
    print(f"Hang cua ma tran: {r}")
    print(f"Co so khong gian Cot (Column Space):\n{c_basis}")
    print(f"Co so khong gian Dong (Row Space):\n{r_basis}")
    print(f"Co so khong gian Nghiem (Null Space):\n{n_basis}")
    print("-" * 30)
    
    verify_rank_and_basis(A_test, r)