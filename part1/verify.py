import numpy as np

# Hàm kiểm tra nghiệm của hệ phương trình Ax = b
def verify_solution(A, my_x, b):
    # 1. Ép kiểu ngay từ đầu
    A_np = np.array(A, dtype=float)
    b_np = np.array(b, dtype=float)

    # 2. Tính rank sử dụng luôn các mảng NumPy vừa ép kiểu cho an toàn
    rank_A = np.linalg.matrix_rank(A_np)
    Ab_np = np.column_stack((A_np, b_np))
    rank_Ab = np.linalg.matrix_rank(Ab_np)

    if rank_A == rank_Ab:
        if my_x is not None: 
            numeric_x = []
            
            # Duyệt qua từng phần tử trong my_x của bạn (Đã sửa lại lề thẳng hàng)
            for item in my_x:
                if isinstance(item, dict):
                    # Nếu là từ điển (vô số nghiệm) -> Lấy giá trị 'const', nếu không có thì mặc định là 0.0
                    numeric_x.append(item.get('const', 0.0))
                else:
                    # Nếu là số bình thường (nghiệm duy nhất) -> Chuyển thành float
                    numeric_x.append(float(item))
                    
            # Ép kiểu list vừa tạo thành mảng NumPy
            x_array = np.array(numeric_x, dtype=float)

            # Dùng A_np và b_np đã ép kiểu để so sánh
            is_correct = np.allclose(A_np @ x_array, b_np, atol=1e-12)
            if is_correct:
                print("=> VERIFICATION SUCCESS: Solution x is correct (A*x == b).")
            else:
                print("=> VERIFICATION FAILED: Solution x is incorrect (A*x != b).")
        else:
            print("=> VERIFICATION FAILED: System has a solution but your function did not find it (returns None).")
            
    else:
        print("NumPy confirms the system is inconsistent (no solution). Skipping allclose verification.")
        if my_x is None:
            print("=> VERIFICATION SUCCESS: Your function also correctly identified the system as inconsistent.")
        else:
            print("=> VERIFICATION FAILED: The system is inconsistent, but your function found a solution.")


# Hàm kiểm tra định thức
def verify_determinant(A, my_det):
    A_np = np.array(A, dtype=float)
    np_det = np.linalg.det(A_np)
    
    print(f"Determinant calculated: {my_det:g}")
    print(f"Determinant of NumPy: {np_det:g}")
    
    if np.isclose(my_det, np_det, atol=1e-12):
        print("=> VERIFICATION SUCCESS: Determinant is correct.")
    else:
        print("=> VERIFICATION FAILED: Determinant is incorrect.")

# Hàm kiểm tra ma trận nghịch đảo
# Cách 1:
def verify_inv_solution(A, A_inv):
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
        
    print(f"1. A * A_inv ≈ I: {'CORRECT' if is_identity else 'INCORRECT'}")
    print(f"2. Matches NumPy: {'CORRECT' if is_correct_with_numpy else 'INCORRECT'}")
    
    return is_identity and is_correct_with_numpy
# Cách 2:
def verify_inverse(A, my_A_inv):
    A_np = np.array(A, dtype=float)    
    try:
        np_A_inv = np.linalg.inv(A_np)
        if my_A_inv is None:
            print("=> VERIFICATION FAILED: Could not find the inverse matrix.")
        else:
            my_inv_np = np.array(my_A_inv, dtype=float)
            is_correct = np.allclose(my_inv_np, np_A_inv, atol=1e-12)
            
            if is_correct:
                print("=> VERIFICATION SUCCESS: Inverse matrix is correct.")
            else:
                print("=> VERIFICATION FAILED: Inverse matrix is incorrect.")
            
    except np.linalg.LinAlgError:
        if my_A_inv is None:
            print("=> VERIFICATION SUCCESS: The matrix is singular (not invertible).")
        else:
            print("=> VERIFICATION FAILED: The matrix is singular (not invertible).")


# Hàm kiểm tra rank
def verify_rank(A, my_rank):
    A_np = np.array(A, dtype=float)
    np_rank = np.linalg.matrix_rank(A_np)
    
    print(f"Rank tự tính: {my_rank}")
    print(f"Rank của NumPy: {np_rank}")
    
    if my_rank == np_rank:
        print("=> VERIFICATION SUCCESS: Rank is correct.")
    else:
        print("=> VERIFICATION FAILED: Rank is incorrect.")