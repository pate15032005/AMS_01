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
                print("=> KIỂM CHỨNG THÀNH CÔNG: Nghiệm x hoàn toàn chính xác.")
            else:
                print("=> KIỂM CHỨNG THẤT BẠI: Nghiệm x tính sai (A*x != b).")
        else:
            print("=> KIỂM CHỨNG THẤT BẠI: Hệ có nghiệm nhưng hàm của bạn không tìm được (trả về None).")
            
    else:
        print("NumPy xác nhận hệ VÔ NGHIỆM. Bỏ qua bước kiểm tra allclose.")
        if my_x is None:
            print("=> KIỂM CHỨNG THÀNH CÔNG: Hàm của bạn cũng kết luận vô nghiệm.")
        else:
            print("=> KIỂM CHỨNG THẤT BẠI: Hệ vô nghiệm mà hàm của bạn lại tính ra nghiệm x.")


# Hàm kiểm tra định thức
def verify_determinant(A, my_det):
    A_np = np.array(A, dtype=float)
    np_det = np.linalg.det(A_np)
    
    print(f"Định thức tự tính: {my_det:g}")
    print(f"Định thức của NumPy: {np_det:g}")
    
    if np.isclose(my_det, np_det, atol=1e-12):
        print("=> KIỂM CHỨNG THÀNH CÔNG: Định thức tính đúng.")
    else:
        print("=> KIỂM CHỨNG THẤT BẠI: Định thức tính sai.")

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
        
    print(f"1. A * A_inv ≈ I: {'ĐÚNG' if is_identity else 'SAI'}")
    print(f"2. Khớp với NumPy: {'ĐÚNG' if is_correct_with_numpy else 'SAI'}")
    
    return is_identity and is_correct_with_numpy
# Cách 2:
def verify_inverse(A, my_A_inv):
    A_np = np.array(A, dtype=float)    
    try:
        np_A_inv = np.linalg.inv(A_np)
        if my_A_inv is None:
            print("=> KIỂM CHỨNG THẤT BẠI: Không tìm ra ma trận nghịch đảo.")
        else:
            my_inv_np = np.array(my_A_inv, dtype=float)
            is_correct = np.allclose(my_inv_np, np_A_inv, atol=1e-12)
            
            if is_correct:
                print("=> KIỂM CHỨNG THÀNH CÔNG.")
            else:
                print("=> KIỂM CHỨNG THẤT BẠI.")
            
    except np.linalg.LinAlgError:
        if my_A_inv is None:
            print("=> KIỂM CHỨNG THÀNH CÔNG: Ma trận suy biến.")
        else:
            print("=> KIỂM CHỨNG THẤT BẠI: Ma trận suy biến.")


# Hàm kiểm tra rank
def verify_rank(A, my_rank):
    A_np = np.array(A, dtype=float)
    np_rank = np.linalg.matrix_rank(A_np)
    
    print(f"Rank tự tính: {my_rank}")
    print(f"Rank của NumPy: {np_rank}")
    
    if my_rank == np_rank:
        print("KẾT QUẢ RANK: CHÍNH XÁC")
    else:
        print("KẾT QUẢ RANK: SAI")