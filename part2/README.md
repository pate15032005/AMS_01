## Folder Structure

```
part2/
│
├── decomposition.py         # Phân rã Cholesky
├── diagonalization.py       # Chéo hóa ma trận
├── eigenvalues_utils.py     # Hàm tính toán trị riêng
├── eigenvector_utils.py     # Hàm tính toán véc tơ riêng
├── main.py                  # Điểm vào để kiểm tra các thuật toán
├── manim_scene.py           # Trực quan hóa bằng manim
│
├── pyproject.toml           # File cấu hình project & dependencies
├── README.md                
│
├── media/                   # Các file media được tạo ra bởi manim (auto-generated)
│   ├── images/
│   ├── Tex/
│   ├── texts/
│   └── videos/
│       └── manim_scene/
│           └── 480p15/
│
├── .venv/                   # (ignored) Môi trường Python ảo
├── __pycache__/             # (ignored) Cache của Python
├── .gitkeep                
├── .python-version        
└── uv.lock                  
```

---
## Yêu cầu môi trường

- Python >= 3.10
- pip

---
## Cài đặt Manim

### 1. Cài uv

```bash
pip install uv
```
### 2. Tạo môi trường ảo

Tại thư mục chứa manim_scene:

```bash
uv venv
```

Kích hoạt môi trường:
- Windows:
```bash
.venv\Scripts\activate
```
- macOS / Linux:
```bash
source .venv/bin/activate
```
### 3. Cài Manim
```bash
uv add manim
```
### 4. Cài thêm dependencies khác
- Cài FFmpeg (nếu chưa có):
	+ Windows: Tải từ https://ffmpeg.org/download.html và thêm vào PATH
	+ macOS: ```brew install ffmpeg```
	+ Linux: ```sudo apt install ffmpeg```

- Cài LaTeX:
	+ Windows: Tải MiKTeX từ https://miktex.org/download
	+ macOS: ```brew install --cask mactex```
	+ Linux: ```sudo apt install texlive-full```

- Cài dependencies của project
```bash
uv sync
```

---

## Cách sử dụng
Gõ các lệnh sau trong terminal để chạy các scene của manim:

- Để chạy scene cụ thể trong manim_scene.py: ```uv run manim -pql manim_scene.py className```
- Để chạy tất cả scene: 
	+ uv run manim -pql manim_scene.py
	+ Chọn số thứ tự tương ứng với scene mình muốn chạy hoặc chọn '*' để chạy tất cả các scene
	+ Lưu ý: Manim không có công cụ để chạy tất cả scene trong một file, nên nó sẽ tự động chạy từng scene một. 
- Lưu ý: ```-pql``` là viết tắt của "preview quality low", nghĩa là chất lượng video sẽ ở mức thấp để render nhanh hơn.
	+ Để xuất video với chất lượng cao hơn, thay đổi ```-pql``` thành ```-pqh``` hoặc ```-pqm``` tùy vào chất lượng mong muốn.
	+ Ví dụ: ```uv run manim -pqh manim_scene.py className```

---
## Output
Video được lưu tại: media/videos/manim_scene/

---
## Lưu ý
- Không cần commit:
.venv/
__pycache__/
media/
- Nếu lỗi render:

  + kiểm tra FFmpeg đã cài chưa

  + kiểm tra LaTeX 

---
## Tham khảo
- Các bước cài đặt thư viện Manim: https://docs.manim.community/en/stable/installation/uv.html