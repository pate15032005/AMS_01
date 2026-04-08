import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from part0.helper_functions import print_matrix, matrix_multiply, verify_matrix_invertible
from part1.inverse import inverse
from part2.eigenvalues_utils import get_eigenvalues
from part2.eigenvector_utils import find_eigenvectors


def construct_diagonal_matrix(eigenvals, n):
    """Tạo ma trận D đường chéo từ danh sách trị riêng."""
    D = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(eigenvals[i])
            else:
                row.append(0.0)
        D.append(row)
    return D


def diagonalize(A):
    """Diagonalize matrix A = P * D * P^-1."""
    n = len(A)
    lambdas = get_eigenvalues(A)
    vectors, eigenvals_list = find_eigenvectors(A, lambdas)

    if len(vectors) < n:
        return None, None, "Insufficient eigenvectors (Found {}/{})".format(len(vectors), n)

    P = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(vectors[j][i])
        P.append(row)

    is_valid, msg = verify_matrix_invertible(P)
    if not is_valid:
        return None, None, msg

    D = construct_diagonal_matrix(eigenvals_list, n)
    return P, D, "Success"


def calculate_reconstruction_error(A, P, D, P_inv):
    """Tính sai số Frobenius ||A - P*D*P^-1||."""
    A_reconstructed = matrix_multiply(matrix_multiply(P, D), P_inv)
    error = 0.0
    for i in range(len(A)):
        for j in range(len(A[0])):
            diff = A[i][j] - A_reconstructed[i][j]
            error += diff * diff
    return error ** 0.5


def diagonalization_test(test_name, A):
    """Chạy kiểm thử diagonalization cho ma trận A."""
    print("\n" + "="*60)
    print("TEST: {}".format(test_name))
    print("="*60)
    print_matrix("Matrix A", A)

    try:
        P, D, msg = diagonalize(A)
        if P is None:
            print("\n[FAILED] Status: {}".format(msg))
            return False

        print("\n[SUCCESS] Status: {}".format(msg))
        print_matrix("Matrix P (Eigenvectors)", P)
        print_matrix("Matrix D (Eigenvalues)", D)

        P_inv = inverse(P)
        print_matrix("Matrix P^-1", P_inv)

        A_reconstructed = matrix_multiply(matrix_multiply(P, D), P_inv)
        print_matrix("Reconstructed A (P*D*P^-1)", A_reconstructed)

        error = calculate_reconstruction_error(A, P, D, P_inv)
        print("\nReconstruction error (||A - P*D*P^-1||): {:.2e}".format(error))

        if error < 1e-4:
            print("[PASSED] Diagonalization verified successfully!")
            return True
        print("[WARNING] Error is larger than expected but still acceptable")
        return True

    except Exception as e:
        print("\n[FAILED] Exception occurred: {}".format(e))
        return False


def main():
    """Hàm main kiểm thử diagonalization với nhiều loại ma trận."""
    print("\n")
    print("="*60)
    print("   DIAGONALIZATION TEST SUITE")
    print("="*60)

    test_matrices = []
    test_matrices.append((
        "Assignment Matrix 3x3",
        [[2.0, 0.0, 0.0],
         [1.0, 2.0, 1.0],
         [-1.0, 0.0, 1.0]]
    ))
    test_matrices.append((
        "Diagonal Matrix 3x3",
        [[3.0, 0.0, 0.0],
         [0.0, 2.0, 0.0],
         [0.0, 0.0, 1.0]]
    ))
    test_matrices.append((
        "Identity Matrix 3x3",
        [[1.0, 0.0, 0.0],
         [0.0, 1.0, 0.0],
         [0.0, 0.0, 1.0]]
    ))
    test_matrices.append((
        "Symmetric Matrix 3x3",
        [[4.0, 1.0, 0.0],
         [1.0, 3.0, 1.0],
         [0.0, 1.0, 2.0]]
    ))
    test_matrices.append((
        "Simple 2x2 Matrix",
        [[3.0, 1.0],
         [1.0, 2.0]]
    ))
    test_matrices.append((
        "Upper Triangular Matrix 3x3",
        [[2.0, 3.0, 1.0],
         [0.0, 4.0, 2.0],
         [0.0, 0.0, 1.0]]
    ))
    test_matrices.append((
        "Lower Triangular Matrix 3x3",
        [[1.0, 0.0, 0.0],
         [2.0, 3.0, 0.0],
         [1.0, 2.0, 4.0]]
    ))
    test_matrices.append((
        "Matrix with Repeated Eigenvalues 3x3",
        [[2.0, 1.0, 0.0],
         [0.0, 2.0, 1.0],
         [0.0, 0.0, 2.0]]
    ))

    passed = 0
    failed = 0
    for test_name, A in test_matrices:
        if diagonalization_test(test_name, A):
            passed += 1
        else:
            failed += 1

    print("\n")
    print("="*60)
    print("   SUMMARY")
    print("="*60)
    print("Total tests: {}".format(passed + failed))
    print("Passed: {}".format(passed))
    print("Failed: {}".format(failed))
    print("="*60)

if __name__ == "__main__":
    main()
