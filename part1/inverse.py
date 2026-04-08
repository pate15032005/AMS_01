from determinant import determinant 


def inverse(A):
    # kiểm tra định thức
    det_A = determinant(A)
    if abs(det_A) < 1e-12:
        raise ValueError("Ma trận không khả nghịch vì định thức bằng 0.")
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