##Readme của Diễm Thúy

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
├── .gitkeep                 # Keeps empty folders tracked
├── .python-version          # Python version (optional)
└── uv.lock                  # Dependency lock file (optional)
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
