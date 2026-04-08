import sys
import os

# Add the root directory to PATH so part0 and part1 can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from part1.rank_basis import rank_and_basis

NULL_SPACE_INDEX = 3
ROUNDING_PRECISIONS = [6, 4]
EIGENVECTOR_TOLERANCE = 1e-8
ZERO_THRESHOLD = 1e-10


def is_duplicate_eigenvector(v1, v2, tolerance=EIGENVECTOR_TOLERANCE):

    """Kiểm tra xem hai vector riêng có đại diện cho cùng một hướng hay không."""

    diff_sum = 0.0

    for i in range(len(v1)):

        diff_sum += abs(v1[i] - v2[i])

    return diff_sum < tolerance



def normalize_eigenvector(v, zero_threshold=ZERO_THRESHOLD):

    """ Chuẩn hóa vector riêng để tránh -0.0 và các giá trị sai số rất nhỏ"""

    result = []

    for val in v:

        if abs(val) < zero_threshold:

            result.append(0.0)

        else:

            result.append(float(val))

    return result

def extract_null_space(res):
    """Lấy không gian nghiệm từ kết quả rank_and_basis."""
    if isinstance(res, dict):
        return res.get('null_space', [])
    elif isinstance(res, (list, tuple)) and len(res) > NULL_SPACE_INDEX:
        return res[NULL_SPACE_INDEX]
    return []


def retry_extract_null_space(A, lambda_val, n):
    """Thử lại tìm null space với các giá trị lambda làm tròn."""
    curr_lam = round(float(lambda_val), 8)

    for precision in ROUNDING_PRECISIONS:
        lam_retry = round(curr_lam, precision)
        M_retry = []
        for i in range(n):
            row = []
            for j in range(n):
                val = float(A[i][j])
                if i == j:
                    val -= lam_retry
                row.append(val)
            M_retry.append(row)

        res_retry = rank_and_basis(M_retry)
        temp_null = extract_null_space(res_retry)
        if temp_null:
            return temp_null
    return []


def group_close_eigenvalues(lambdas, tolerance=1e-5):
    """Nhóm các trị riêng gần nhau để giảm sai số số học."""
    grouped = []
    for l in lambdas:
        placed = False
        for group in grouped:
            if abs(l - group[0]) < tolerance:
                group.append(l)
                placed = True
                break
        if not placed:
            grouped.append([l])

    result = []
    for group in grouped:
        avg = sum(group) / float(len(group))
        result.append(float(round(avg, 8)))
    return result


def form_shifted_matrix(A, lambda_val):
    """Tạo ma trận A - lambda*I để tính null space."""
    n = len(A)
    curr_lam = round(float(lambda_val), 8)

    M = []
    for i in range(n):
        row = []
        for j in range(n):
            val = float(A[i][j])
            if i == j:
                val -= curr_lam
            row.append(val)
        M.append(row)
    return M


def find_eigenvectors_for_lambda(A, lam, n):
    """Tìm các vector riêng tương ứng trị riêng lam."""
    M = form_shifted_matrix(A, lam)
    res = rank_and_basis(M)
    null_space = extract_null_space(res)

    if not null_space:
        null_space = retry_extract_null_space(A, lam, n)
    return null_space


def find_eigenvectors(A, lambdas):
    """Tạo danh sách vector riêng cho tất cả trị riêng."""
    n = len(A)
    vectors = []
    eigenvals = []

    unique_lambdas = group_close_eigenvalues(lambdas)

    for lam in unique_lambdas:
        null_space = find_eigenvectors_for_lambda(A, lam, n)
        for v in null_space:
            normalized_v = normalize_eigenvector(v)
            is_duplicate = False
            for existing_v in vectors:
                if is_duplicate_eigenvector(normalized_v, existing_v):
                    is_duplicate = True
                    break
            if not is_duplicate:
                vectors.append(normalized_v)
                eigenvals.append(lam)
    return vectors, eigenvals
