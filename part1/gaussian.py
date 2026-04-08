import copy # Tạo bản sao của ma trận, tránh làm biến đổi ma trận không mong muốn

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
                return None # Hệ phương trình vô nghiệm
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

def gaussian_eliminate(A, b):
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

    x = back_substitution(A_work, b_work)

    return A_work, x, swaps

