import copy

def determinant(A):
    """
    Tính định thức của ma trận vuông bằng cách khử Gauss.
    Trả về giá trị định thức của ma trận.
    """

    # Tạo bản sao    
    n = len(A)
    if n == 0 or any(len(row) != n for row in A):
        raise ValueError("Không thể tính định thức của ma trận này")

    A_work = copy.deepcopy(A)
    det = 1.0
    swaps = 0
    
    for i in range(n):
        # Chọn phần tử trội (Partial Pivoting)
        max_row = i
        for k in range(i + 1, n):
            if abs(A_work[k][i]) > abs(A_work[max_row][i]):
                max_row = k

        # Hoán đổi hàng i với hàng có phần tử lớn nhất, tăng swaps lên 1
        if i != max_row:
            A_work[i], A_work[max_row] = A_work[max_row], A_work[i]
            swaps += 1
        det *= A_work[i][i]

        # Kiểm tra nếu phần tử chốt quá nhỏ (định thức = 0)
        if abs(A_work[i][i]) < 1e-12:
            return 0.0

        # Loại bỏ các phần tử bên dưới phần tử chốt
        for k in range(i + 1, n):
            factor = A_work[k][i] / A_work[i][i]
            for j in range(i, n):
                if i == j:
                    A_work[k][j] = 0
                else:
                    A_work[k][j] -= factor * A_work[i][j]

    return det * (-1) ** swaps

