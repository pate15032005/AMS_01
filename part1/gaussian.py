import copy # Tạo bản sao của ma trận, tránh làm biến đổi ma trận không mong muốn

def forward_substitution(L, c):
    """
    Giải hệ phương trình tuyến tính Lx = c sau khi sử dụng phương pháp Cholesky.
    Giải hệ tam giác dưới
    """
    rows = len(L)
    cols = len(L[0])
    
    # do do L kha nghich, nen x la mot vector chi chua cac hang so, khong chua cac t_i
    x = [0.0] * cols
    for i in range(rows):
        sum_known = 0.0
        for j in range(i):
            sum_known += L[i][j] * x[j]
        x[i] = (c[i] - sum_known) / L[i][i]
    return x



from fractions import Fraction

def back_substitution(U, c, use_fraction=False):
    """
    Giải hệ phương trình tuyến tính Ux = c (hệ tam giác trên).
    Hỗ trợ nghiệm duy nhất và nghiệm tổng quát (vô số nghiệm).
    
    Args:
        U: Ma trận bậc thang (REF).
        c: Vector hằng số tương ứng.
        use_fraction: Nếu True, sử dụng số học phân số (sai số = 0).
    """
    rows = len(U)
    cols = len(U[0])
    
    # Thiết lập giá trị cơ sở và ngưỡng sai số dựa trên chế độ tính toán
    zero = Fraction(0) if use_fraction else 0.0
    one = Fraction(1) if use_fraction else 1.0
    eps = 0 if use_fraction else 1e-14

    # Khởi tạo x: mặc định mọi biến đều là biến tự do t_j (x_j = 0 + 1*t_j)
    # Nếu biến nào có phần tử chốt (pivot), nó sẽ bị ghi đè bằng công thức cụ thể
    x = [{'const': zero, f't_{j}': one} for j in range(cols)]
    
    # Duyệt từ dòng cuối cùng lên đầu
    for i in range(rows - 1, -1, -1):
        # 1. Tìm cột chứa phần tử chốt (pivot) của dòng i
        pivot_col = -1
        for j in range(cols):
            if abs(U[i][j]) > eps:
                pivot_col = j
                break 
        
        # 2. Xử lý trường hợp dòng không có pivot (dòng toàn số 0)
        if pivot_col == -1: 
            if abs(c[i]) > eps:
                return None  # Dòng 0 = số khác 0 -> Hệ vô nghiệm
            continue  # Dòng 0 = 0 -> Bỏ qua dòng này

        # 3. Tính tổng các biến đã biết (biến ở các cột bên phải pivot)
        # sum_known sẽ là một từ điển tổng hợp: const + t_a*val_a + t_b*val_b...
        sum_known = {'const': zero}
        for j in range(pivot_col + 1, cols):
            factor = U[i][j]
            # Nhân hệ số U[i][j] vào từng thành phần của x[j]
            for key, val in x[j].items():
                sum_known[key] = sum_known.get(key, zero) + factor * val

        # 4. Giải tìm biến tại cột pivot: x[pivot_col] = (c[i] - sum_known) / pivot_val
        pivot_val = U[i][pivot_col]
        
        # Thành phần hằng số
        new_x = {'const': (c[i] - sum_known.get('const', zero)) / pivot_val}
        
        # Thành phần biến tự do (các t_k)
        for key, val in sum_known.items():
            if key != 'const':
                # Chuyển vế đổi dấu và chia cho pivot_val
                new_val = -val / pivot_val
                # Chỉ giữ lại những tham số có giá trị khác eps
                if abs(new_val) > eps:
                    new_x[key] = new_val

        # Cập nhật lại x[pivot_col]. Lúc này nó trở thành biến phụ thuộc.
        x[pivot_col] = new_x
        
    return x

def gaussian_eliminate(A, b, use_fraction=False):
    """
    Thực hiện phép khử Gauss để đưa ma trận A về dạng bậc thang (REF).
    Trả về ma trận đã được khử, nghiệm (dưới dạng list of dict), và số lần hoán đổi dòng.
    Nếu use_fraction=True, sử dụng số học phân số để tránh sai số làm hỏng
    kết quả nghiệm.
    Args:
        A: Ma trận hệ số (danh sách các danh sách).
        b: Vector hằng số (danh sách).
        use_fraction: Nếu True, sử dụng số học phân số (sai số = 0).
    """
    A_work = copy.deepcopy(A)
    b_work = copy.deepcopy(b)
    
    rows = len(A_work)
    cols = len(A_work[0]) 
    swaps = 0
    r = 0
    c = 0
    
    if use_fraction:
        A_work = [[Fraction(A_work[i][j]) for j in range(cols)] for i in range(rows)]
        b_work = [Fraction(b_work[i]) for i in range(rows)]
        eps = 0
    else:
        eps = 1e-14
    
    while r < rows and c < cols:
        max_row = r
        for k in range(r + 1, rows):
            if abs(A_work[k][c]) > abs(A_work[max_row][c]):
                max_row = k
                
        if abs(A_work[max_row][c]) < eps:
            c += 1
            continue

        if r != max_row:   
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

    x = back_substitution(A_work, b_work, use_fraction)
    return A_work, x, swaps



    
