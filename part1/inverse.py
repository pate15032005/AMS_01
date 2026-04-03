import numpy as np

#de day den khi Thien code xong (3)
def determinant(A):
    matrix = np.array(A, dtype=float)
    n = matrix.shape[0]
    s = 0  
    det = 1.0

    for i in range(n):
        max_row = i + np.argmax(np.abs(matrix[i:, i]))
        
        if np.abs(matrix[max_row, i]) < 1e-12:
            return 0.0 
        
        if max_row != i:
            matrix[[i, max_row]] = matrix[[max_row, i]]
            s += 1
        
        det *= matrix[i, i]
        
        for j in range(i + 1, n):
            factor = matrix[j, i] / matrix[i, i]
            matrix[j] -= factor * matrix[i]

    return ((-1) ** s) * det 

def inverse(A):
    det_A = determinant(A)
    #so sanh voi esilon vi khi tinh det bang float co the ra 0.00000000abc thi khong the so sanh voi 0 duoc
    if np.abs(det_A) < 1e-12:
        raise ValueError("Ma tran khong kha nghich vi dinh thuc bang 0.")
    
    #tao ma tran ep kieu float
    matrix = np.array(A, dtype= float) 
    n = matrix.shape[0] 
    
    #ghep ma tran
    combined = np.hstack((matrix, np.eye(n)))
    
    #bien doi so cap
    for i in range(n):
        # partial pivoting 
        max_row = i + np.argmax(np.abs(combined[i:, i])) #chon dong chua phan tu lon nhat cua cot 
        combined[[i, max_row]] = combined[[max_row, i]] # hoan doi dong do voi dong dang xet

        # dua pivot ve 1
        pivot = combined[i, i] 
        combined[i] /= pivot 

        # khu cac phan tu
        for j in range(n):
            if i != j:
                factor = combined[j, i]
                combined[j] -= factor * combined[i] #dong j tru 1 factor dong i 
    
    #tra ve A^-1
    return combined[:, n:] 
    
    #vibe code test thu 

def verify_solution(A, A_inv):
    A = np.array(A, dtype=float)
    n = A.shape[0]
    
    identity_check = np.dot(A, A_inv)
    I = np.eye(n)
    
    is_identity = np.allclose(identity_check, I, atol=1e-8)
    
    try:
        np_inv = np.linalg.inv(A)
        is_correct_with_numpy = np.allclose(A_inv, np_inv, atol=1e-8)
    except np.linalg.LinAlgError:
        is_correct_with_numpy = False 
    print(f"1. A * A_inv ≈ I: {'ĐÚNG' if is_identity else 'SAI'}")
    print(f"2. Khớp với NumPy: {'ĐÚNG' if is_correct_with_numpy else 'SAI'}")
    
    return is_identity and is_correct_with_numpy

if __name__ == "__main__":
    A_test = [[0, 2, 1], 
              [1, -1, 1], 
              [2, 4, 2]]

    try:
        my_inv = inverse(A_test) 
        print("Ma trận nghịch đảo tự tính:\n", my_inv)
        
        verify_solution(A_test, my_inv)
    except Exception as e:
        print(f"Lỗi: {e}")