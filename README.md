# 🎓 AMS_01: Đồ Án Ma Trận và Cơ Sở Tính Toán Khoa Học

**Tiêu đề:** MA TRẬN VÀ CƠ SỞ TÍNH TOÁN KHOA HỌC  
**Lớp học:** TUDTK (Tính Toán Khoa Học)  
**Năm học:** 2025-2026

---

## 📋 Mục Tiêu Dự Án

Dự án này triển khai và minh họa các thuật toán cơ bản trong đại số tuyến tính và tính toán khoa học:

✅ **Part 1:** Giải hệ phương trình tuyến tính (Gaussian Elimination)  
✅ **Part 2:** Eigenvalue, Eigenvector, và Diagonalization  
✅ **Part 3:** So sánh các phương pháp giải (Gaussian, Gauss-Seidel, Cholesky)  
✅ **Visualization:** Tạo animation toán học bằng Manim

---

## 📂 Cấu Trúc Dự Án

```
AMS_01/
│
├── part0/                          # Hàm tiện ích chung
│   └── helper_functions.py         # Các hàm phụ trợ (in ma trận, nhân ma trận, etc.)
│
├── part1/                          # Giải hệ phương trình tuyến tính
│   ├── gaussian.py                 # Khử Gauss (Gaussian Elimination)
│   ├── determinant.py              # Tính định thức
│   ├── inverse.py                  # Tìm ma trận nghịch đảo
│   ├── rank_basis.py               # Tính hạng và cơ sở ma trận
│   ├── verify.py                   # Kiểm chứng kết quả
│   ├── part1_demo.ipynb            # Notebook minh họa
│   └── __pycache__/
│
├── part2/                          # Eigenvalue, Eigenvector, Diagonalization
│   ├── decomposition.py            # Phân rã Cholesky
│   ├── diagonalization.py          # Chéo hóa ma trận
│   ├── eigenvalues_utils.py        # Tính trị riêng
│   ├── eigenvector_utils.py        # Tính véc tơ riêng
│   ├── main.py                     # Kiểm tra các thuật toán
│   ├── manim_scene.py              # Trực quan hóa bằng Manim
│   ├── pyproject.toml              # Dependencies của Manim
│   ├── README.md                   # Hướng dẫn riêng cho Part 2
│   ├── media/                      # (auto-generated) Các file media từ Manim
│   └── __pycache__/
│
├── part3/                          # So sánh các phương pháp giải
│   ├── solver.py                   # Cài đặt 3 phương pháp giải
│   ├── benchmark.py                # So sánh hiệu suất
│   ├── analysis.ipynb              # Phân tích kết quả
│   └── __pycache__/
│
├── report/                         # Báo cáo
│
├── requirements.txt                # Dependencies của toàn bộ dự án
├── README.md                       # File này
└── TUD-TK Do An 01 - Ma tran.pdf   # Tài liệu đề bài
```

---

## 🔧 Yêu Cầu Hệ Thống

- **Python:** >= 3.11
- **pip:** (trình quản lý package)
- **Jupyter:** (để chạy notebook)

---

## 💾 Cài Đặt

### 1. Clone Repository
```bash
git clone <repo-url>
cd AMS_01
```

### 2. Cài Đặt Dependencies

```bash
pip install -r requirements.txt
```

**Dependencies chính:**
- `numpy>=1.24.0` - Tính toán ma trận
- `manim>=0.20.1` - Animation toán học
- `scipy>=1.10.0` - Thư viện khoa học
- `matplotlib>=3.5.0` - Vẽ đồ thị
- `jupyter>=1.0.0` - Chạy Jupyter Notebook
- `ipython>=8.0.0` - Interactive Python

### 3. (Tùy chọn) Cài Đặt Manim cho Part 2

Nếu bạn muốn chạy Manim animations:

```bash
cd part2
pip install -e ".[manim]"
```

---

## 📖 Hướng Dẫn Sử Dụng

### **Part 1: Giải Hệ Phương Trình Tuyến Tính**

Bao gồm các thuật toán:
- **Khử Gauss (Gaussian Elimination)** - Phương pháp trực tiếp
- **Tính Định Thức** - Dùng để kiểm tra tính khả nghịch
- **Ma Trận Nghịch Đảo** - Inverse matrix
- **Hạng và Cơ Sở** - Rank and Basis

#### Chạy Demo:
```bash
cd part1
jupyter notebook part1_demo.ipynb
```

Hoặc chạy từ terminal:
```bash
python -c "from gaussian import gaussian_eliminate; help(gaussian_eliminate)"
```

**Test Cases:**
- ✅ Hệ có nghiệm duy nhất
- ✅ Hệ có vô số nghiệm
- ✅ Hệ vô nghiệm

---

### **Part 2: Eigenvalue, Eigenvector, Diagonalization**

Triển khai:
- **Tính Trị Riêng (Eigenvalues)** - Dùng power iteration
- **Tính Véc Tơ Riêng (Eigenvectors)**
- **Chéo Hóa Ma Trận (Diagonalization)** - A = PDP⁻¹
- **Phân Rã Cholesky** - Cho ma trận xác định dương

#### Chạy Demo:
```bash
cd part2
python main.py
```

#### Tạo Animation:
```bash
cd part2
manim -pql manim_scene.py CholeskyForm
```

Xem chi tiết hơn tại [part2/README.md](part2/README.md)

---

### **Part 3: So Sánh Các Phương Pháp Giải**

So sánh hiệu suất của 3 phương pháp:
1. **Gaussian Elimination** - Phương pháp trực tiếp
2. **Gauss-Seidel** - Phương pháp lặp
3. **Cholesky** - Phân rã cho ma trận SPD (Symmetric Positive Definite)

#### Chạy Benchmark:
```bash
cd part3
python benchmark.py
```

#### Xem Phân Tích:
```bash
cd part3
jupyter notebook analysis.ipynb
```

---

## 🎯 Nội Dung Chi Tiết

### Part 0: Helper Functions

Các hàm tiện ích dùng chung:
- `print_matrix(title, M)` - In ma trận đẹp mắt
- `matrix_multiply(A, B)` - Nhân ma trận
- `matrix_subtract(A, B)` - Trừ ma trận
- `create_identity(n)` - Tạo ma trận đơn vị
- `get_trace(A)` - Tính vết (trace)
- `matrix_transpose(A)` - Chuyển vị ma trận

### Part 1: Giải Hệ Phương Trình

#### Khử Gauss:
```python
from part1.gaussian import gaussian_eliminate

A = [[2, 1, -1], [-3, -1, 2], [-2, 1, 2]]
b = [8, -11, -3]

U, x, swaps = gaussian_eliminate(A, b, use_fraction=True)
```

#### Tính Định Thức:
```python
from part1.determinant import determinant

det = determinant(A)
print(f"Định thức: {det}")
```

#### Tìm Ma Trận Nghịch Đảo:
```python
from part1.inverse import inverse

try:
    A_inv = inverse(A)
    print("Ma trận nghịch đảo:", A_inv)
except ValueError:
    print("Ma trận không khả nghịch")
```

#### Tính Hạng và Cơ Sở:
```python
from part1.rank_basis import rank_and_basis

rank, col_basis, row_basis, null_basis = rank_and_basis(A)
print(f"Hạng: {rank}")
```

### Part 2: Eigenvalue và Diagonalization

#### Tính Trị Riêng:
```python
from part2.eigenvalues_utils import get_eigenvalues

eigenvalues = get_eigenvalues(A, num_iterations=1000)
print("Trị riêng:", eigenvalues)
```

#### Tính Véc Tơ Riêng:
```python
from part2.eigenvector_utils import find_eigenvectors

eigenvectors = find_eigenvectors(A, eigenvalues)
```

#### Chéo Hóa:
```python
from part2.diagonalization import diagonalize

P, D = diagonalize(A)
```

#### Phân Rã Cholesky:
```python
from part2.decomposition import cholesky

L = cholesky(A)
print("Ma trận Cholesky L:", L)
```

### Part 3: So Sánh Phương Pháp Giải

```python
from part3.solver import solve_gaussian, solve_gauss_seidel, solve_cholesky

A = [[4, 1], [1, 3]]
b = [1, 2]

# Gaussian Elimination
x1 = solve_gaussian(A, b)

# Gauss-Seidel (lặp)
x2 = solve_gauss_seidel(A, b, max_iter=100)

# Cholesky (cho ma trận SPD)
x3 = solve_cholesky(A, b)

print(f"Gaussian: {x1}")
print(f"Gauss-Seidel: {x2}")
print(f"Cholesky: {x3}")
```

---

## 📊 Jupyter Notebooks

Dự án bao gồm các notebook để minh họa:

1. **part1/part1_demo.ipynb** - Demo Part 1 (Giải hệ phương trình)
   - Test case: Hệ có nghiệm duy nhất
   - Test case: Hệ có vô số nghiệm
   - Test case: Hệ vô nghiệm

2. **part3/analysis.ipynb** - Phân tích hiệu suất Part 3
   - So sánh 3 phương pháp giải
   - Visualize kết quả

#### Chạy Notebook:
```bash
jupyter notebook part1/part1_demo.ipynb
```

---

## 🐛 Troubleshooting

### Lỗi: `ModuleNotFoundError: No module named 'part1'`

**Giải pháp:** Đảm bảo đã cài `sys.path` correctly hoặc chạy từ thư mục gốc:
```bash
cd /path/to/AMS_01
python -c "import part1"
```

### Lỗi: Manim không cài được trên Windows

**Giải pháp:** Cài riêng dependencies:
```bash
pip install manim pycairo
```

### Lỗi: Jupyter Notebook không tìm được module

**Giải pháp:** Chạy notebook từ thư mục gốc project:
```bash
cd AMS_01
jupyter notebook part1/part1_demo.ipynb
```

---

## 📝 Ghi Chú

- Tất cả các hàm được cài đặt từ đầu (không dùng thư viện cao cấp như `numpy.linalg`)
- Code có đầy đủ docstring và comment tiếng Việt
- Sử dụng `Fraction` để tính toán chính xác (không có lỗi làm tròn)
- Mỗi part có thể chạy độc lập

---

## 👥 Thông Tin Đồ Án

- **Yêu cầu:** Phải cài đặt tất cả hàm từ đầu
- **Định dạng:** Python, Jupyter Notebook
- **Trực quan hóa:** Manim (tạo animation)
- **Kiểm chứng:** Đối chiếu với NumPy/SciPy

---

## 📚 Tài Liệu Tham Khảo

- Tài liệu đề bài: [TUD-TK Do An 01 - Ma tran.pdf](TUD-TK%20Do%20An%2001%20-%20Ma%20tran.pdf)
- Manim Documentation: https://docs.manim.community/
- NumPy Linear Algebra: https://numpy.org/doc/stable/reference/routines.linalg.html

---

## ✨ Hướng Dẫn Đóng Góp

Để cải thiện dự án:

1. Fork repository
2. Tạo branch mới: `git checkout -b feature/improvement`
3. Commit changes: `git commit -am 'Add improvement'`
4. Push: `git push origin feature/improvement`
5. Tạo Pull Request

---

**Last Updated:** April 30, 2026  
**Status:** ✅ Complete

