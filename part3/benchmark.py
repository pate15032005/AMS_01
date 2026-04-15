from solver import solve_cholesky, solve_gauss_seidel, solve_gaussian
import time
import numpy as np

def create_random_spd_matrix(n):
    """Tạo ma trận đối xứng dương xác định ngẫu nhiên kích thước n x n."""
    A = np.random.rand(n, n)
    return np.dot(A, A.T) + n * np.eye(n)  # Đảm bảo ma trận là SPD

def create_hilbert_matrix(n):
    """Tạo ma trận Hilbert kích thước n x n."""
    return np.array([[1/(i+j-1) for j in range(1, n+1)] for i in range(1, n+1)])

def create_random_vector(n):
    """Tạo vector ngẫu nhiên kích thước n."""
    return np.random.rand(n)

def benchmark_solver(solver_func, A, b, **kwargs):
    """Đo thời gian giải hệ phương trình tuyến tính Ax = b bằng solver_func."""
    start_time = time.time()
    x = solver_func(A, b, **kwargs) 
    # **kwargs cho phép truyền thêm các tham số như tol, max_iterations, use_fraction nếu cần
    end_time = time.time()
    return end_time - start_time, x

if __name__ == "__main__":
    sizes = [50, 100, 200, 500, 1000]  # Kích thước ma trận để benchmark
    for n in sizes:
        print(f"Benchmarking with size: {n}x{n}")
        
        # Tạo ma trận và vector
        A_spd = create_random_spd_matrix(n)
        A_hilbert = create_hilbert_matrix(n)
        b = create_random_vector(n)
        
        # Benchmark Cholesky cho ma trận SPD
        time_cholesky, _ = benchmark_solver(solve_cholesky, A_spd, b)
        print(f"Cholesky decomposition time: {time_cholesky:.6f} seconds")

        # Benchmark Cholesky cho ma trận Hilbert (nếu có thể giải được)
        try:
            time_cholesky_hilbert, _ = benchmark_solver(solve_cholesky, A_hilbert, b)
            print(f"Cholesky decomposition (Hilbert) time: {time_cholesky_hilbert:.6f} seconds")
        except ValueError:
            print("Cholesky decomposition failed for Hilbert matrix (not positive definite).")
        
        # Benchmark Gauss-Seidel cho ma trận SPD
        time_gauss_seidel, _ = benchmark_solver(solve_gauss_seidel, A_spd, b, tol=1e-12, max_iterations=1000)
        print(f"Gauss-Seidel time: {time_gauss_seidel:.6f} seconds")

        # Benchmark Gauss-Seidel cho ma trận Hilbert (nếu có thể giải được)
        try:
            time_gauss_seidel_hilbert, _ = benchmark_solver(solve_gauss_seidel, A_hilbert, b, tol=1e-12, max_iterations=1000)
            print(f"Gauss-Seidel (Hilbert) time: {time_gauss_seidel_hilbert:.6f} seconds")
        except ValueError:
            print("Gauss-Seidel failed for Hilbert matrix.")

        # Benchmark Gaussian elimination cho ma trận SPD
        time_gaussian, _ = benchmark_solver(solve_gaussian, A_spd, b)
        print(f"Gaussian elimination time: {time_gaussian:.6f} seconds")
        
        # Benchmark Gaussian elimination cho ma trận Hilbert
        time_gaussian_hilbert, _ = benchmark_solver(solve_gaussian, A_hilbert, b)
        print(f"Gaussian elimination (Hilbert) time: {time_gaussian_hilbert:.6f} seconds")

        # Note: Gaussian elimination with fractions sẽ rất chậm cho ma trận lớn, đặc biệt là ma trận Hilbert
        #       nên có thể bỏ qua hoặc chỉ chạy với kích thước nhỏ hơn để tránh thời gian chạy quá lâu.
        # Benchmark Gaussian elimination với phân số cho ma trận Hilbert
        # time_gaussian_frac, _ = benchmark_solver(solve_gaussian, A_hilbert, b, use_fraction=True)
        # print(f"Gaussian elimination with fractions (Hilbert) time: {time_gaussian_frac:.6f} seconds")   
        
        print("-" * 40)