import copy #tạo bản sao của ma trận, tránh làm biến dổi ma trận không mong muốn

def back_substitution(U, c):
    """
    Giải hệ phương trình tuyến tính Ux = c sau khi sử dụng phương pháp Khử Gauss.
    Giải hệ tam giác trên
    """

    rows = len(U)
    cols = len(U[0])
    
    x = [{'const': 0.0, f't_{j}': 1.0} for j in range(cols)]
    
    for i in range(rows - 1, -1, -1):
        
        pivot_col = -1
        for j in range(cols):
            if abs(U[i][j]) > 1e-12:
                pivot_col = j
                break # Tìm thấy phần tử khác 0 đầu tiên -> Đó là chốt!
        if pivot_col == -1: 
            if abs(c[i]) > 1e-12:
                raise ValueError(f"Hệ vô nghiệm (Mâu thuẫn tại dòng {i}: 0 = {c[i]}).")
            continue 

        sum_known = {'const': 0.0}
        
        for j in range(pivot_col + 1, cols):
            factor = U[i][j]
            for key, val in x[j].items():
                sum_known[key] = sum_known.get(key, 0.0) + factor * val
                

        pivot_val = U[i][pivot_col]
        new_x = {'const': (c[i] - sum_known.get('const', 0.0)) / pivot_val}
        
        for key, val in sum_known.items():
            if key != 'const':
                new_x[key] = -val / pivot_val

        x[pivot_col] = new_x
        
    return x

def gauss_eliminate(A, b):
    """
    Giải hệ phương trình tuyến tính Ax = b bằng phương pháp Khử Gauss.
    Bước 1: Khử xuôi đưa về ma trận tam giác trên.
    Bước 2: Thế ngược để tìm nghiệm x.
    """
    A_work = copy.deepcopy(A)
    b_work = copy.deepcopy(b)
    
    rows = len(A_work)
    cols = len(A_work[0]) 
    swaps = 0
    r = 0
    c = 0
    
    while r < rows and c < cols:
        max_row = r
        for k in range(r + 1, rows):
            if abs(A_work[k][c]) > abs(A_work[max_row][c]):
                max_row = k
                
        # 2. Nếu cột toàn 0 -> Bỏ qua cột này, nhích sang cột kế tiếp
        if abs(A_work[max_row][c]) < 1e-12:
            c += 1
            continue
        if r !=max_row:   
            A_work[r], A_work[max_row] = A_work[max_row], A_work[r]
            b_work[r], b_work[max_row] = b_work[max_row], b_work[r]
            swaps += 1
        
        for k in range(r+1, rows):
            factor = A_work[k][c] / A_work[r][c]
            for j in range(c, cols):
                A_work[k][j] -= factor * A_work[r][j]
            b_work[k] -= factor * b_work[r]
        r += 1
        c += 1
    try:    
        x = back_substitution(A_work, b_work)
    except ValueError as e:
        x = [None]*cols

    return A_work, x, swaps

# Hàm test hiển thị kết quả
def print_solution(x):
    if x[0] is None:
        print("Hệ phương trình vô nghiệm.\n")
        return
        
    for i, expr in enumerate(x):
        terms = []
        const_val = expr.get('const', 0)
        
        # In hằng số nếu nó khác 0 hoặc nếu nó là thành phần duy nhất
        if abs(const_val) > 1e-12 or len(expr) == 1:
            terms.append(str(round(const_val, 4)))
            
        # In các biến tham số t_i
        for key, val in expr.items():
            if key != 'const' and abs(val) > 1e-12:
                sign = "+" if val > 0 else "-"
                # Định dạng hệ số đẹp (bỏ số 1.0 nếu có)
                coeff = f"{abs(round(val, 4))}*" if abs(abs(val) - 1.0) > 1e-12 else ""
                terms.append(f"{sign} {coeff}{key}")
                
        # Ghép chuỗi lại
        expr_str = " ".join(terms)
        if expr_str.startswith("+ "): 
            expr_str = expr_str[2:]
            
        print(f"x_{i} = {expr_str}")
    print()

# ==========================================
# CHẠY THỬ CÁC TRƯỜNG HỢP KHÁC NHAU
# ==========================================

print("--- TEST 1: HỆ CÓ NGHIỆM DUY NHẤT ---")
A1 = [[2, 1, -1], [-3, -1, 2], [-2, 1, 2]]
b1 = [8, -11, -3]
_, x1, _ = gauss_eliminate(A1, b1)
print_solution(x1)

print("--- TEST 2: HỆ VÔ SỐ NGHIỆM (HỆ THIẾU) ---")
# 2 phương trình, 3 ẩn
A2 = [[1, 2, 3], [4, 9, 6]]
b2 = [1, 2]
_, x2, _ = gauss_eliminate(A2, b2)
print_solution(x2)

print("--- TEST 3: HỆ VÔ NGHIỆM ---")
A3 = [[1, 1], [1, 1]]
b3 = [5, 10]
_, x3, _ = gauss_eliminate(A3, b3)
print_solution(x3)

print("--- TEST 4: HỆ THỪA PHƯƠNG TRÌNH CÓ NGHIỆM DUY NHẤT ---")
# 3 hàng, 2 cột
A4 = [
    [1, 1], 
    [1, -1], 
    [2, 1]
]
b4 = [3, -1, 4]

_, x4, _ = gauss_eliminate(A4, b4)
print_solution(x4) 
# Kỳ vọng: x_0 = 1.0, x_1 = 2.0


print("--- TEST 5: HỆ THỪA PHƯƠNG TRÌNH VÔ NGHIỆM ---")
# 3 hàng, 2 cột
A5 = [
    [1, 1], 
    [1, -1], 
    [1, 1]
]
b5 = [3, -1, 10] # Dòng 3 mâu thuẫn dòng 1

_, x5, _ = gauss_eliminate(A5, b5)
print_solution(x5)

