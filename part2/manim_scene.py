from manim import *

class Intro(Scene):
    def construct(self):
        self.camera.background_color = BLACK
        title = Text("Matrix Factorization", font_size = 60)
        subtitle = Text("Cholesky Method", font_size = 30).next_to(title, DOWN)       
        self.play(Write(title))
        self.play(Write(subtitle))
        self.wait()

class SPDExplain(Scene):
     def construct(self):
        self.camera.background_color = BLACK

        # Title
        title = Text("Positive Definite Matrices", font_size=50)
        title.to_edge(UP)

        line = Line(LEFT*5, RIGHT*5).next_to(title, DOWN)

        self.play(Write(title), Create(line))
        self.wait()

        # Description
        desc = MathTex(
            r"\text{A matrix } A \in \mathbb{R}^{n \times n} \text{ is positive definite if:}"
        )
        desc.next_to(line, DOWN, buff=0.8)
        desc.align_to(line, LEFT)

        self.play(Write(desc))
        self.wait()

        # Condition (highlight vàng)
        cond = MathTex(r"(i)\ \text{it is symmetric; } A^T = A")
        cond.set_color(BLUE)
        cond.next_to(desc, DOWN)
        cond.align_to(desc, LEFT)

        self.play(Write(cond))
        self.wait()

        # Matrix
        matrix = Matrix([
            [4, 2, 2],
            [2, 5, 1],
            [2, 1, 3]
        ])

        matrix.next_to(cond, DOWN, buff=1)

        self.play(Write(matrix))
        self.wait()

        entries = matrix.get_entries()

        #Vẽ đường chéo
        diag = Line(
            matrix.get_corner(UL),
            matrix.get_corner(DR),
            color=BLUE
        )
        self.play(Create(diag))
        self.wait()

        #Highlight cặp đối xứng (0,1) & (1,0)
        self.play(
            entries[1].animate.set_color(YELLOW),
            entries[3].animate.set_color(YELLOW),
        )

        line1 = Line(
            entries[1].get_center(),
            entries[3].get_center(),
            color=YELLOW,
            stroke_width=2
        )
        self.play(Create(line1))
        self.wait()

        #Highlight cặp đối xứng (0,2) & (2,0)
        self.play(
            entries[2].animate.set_color(GREEN),
            entries[6].animate.set_color(GREEN)
        )

        line2 = Line(
            entries[2].get_center(),
            entries[6].get_center(),
            color=GREEN,
            stroke_width=2
        )
        self.play(Create(line2))
        self.wait()

        #Highlight cặp đối xứng (1,2) & (2,1)
        self.play(
            entries[5].animate.set_color(RED),
            entries[7].animate.set_color(RED)
        )

        line3 = Line(
            entries[5].get_center(),
            entries[7].get_center(),
            color=RED,
            stroke_width=2
        )
        self.play(Create(line3))
        self.wait()

        #Ma trận biến mất 
        self.play(
            FadeOut(matrix),
            FadeOut(diag),
            FadeOut(line1),
            FadeOut(line2),
            FadeOut(line3)
        )
        self.wait()

        #Đưa (i) về màu trắng
        self.play(cond.animate.set_color(WHITE))
        self.wait()
        #Thêm (ii) với màu xanh
        cond2 = MathTex(
            r"(ii)\ \text{Given } \mathbf{x} \in \mathbb{R}^n \text{ and } \mathbf{x} \neq 0;"
        )
        cond2.set_color(BLUE)

        cond2.next_to(cond, DOWN)
        cond2.align_to(cond, LEFT)

        self.play(Write(cond2))
        self.wait()

        # Thêm dòng công thức
        formula = MathTex(r"\mathbf{x}^T A \mathbf{x} > 0")
        formula.set_color(GREEN)

        formula.next_to(cond2, DOWN)

        self.play(Write(formula))
        self.wait()

class CholeskyForm(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        #Matrix A
        A = MathTex(
            r"\begin{bmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\"
            r"a_{21} & a_{22} & \cdots & a_{2n} \\"
            r"\vdots & \vdots & \ddots & \vdots \\"
            r"a_{n1} & a_{n2} & \cdots & a_{nn} \end{bmatrix}"
        )

        label_A = MathTex("A")
        group_A = VGroup(label_A, A).arrange(DOWN)

        #Dấu =
        eq = MathTex("=")

        #L (lower triangular)
        L = MathTex(
            r"\begin{bmatrix} 1 & 0 & \cdots & 0 \\"
            r"\ast & 1 & \cdots & 0 \\"
            r"\vdots & \vdots & \ddots & \vdots \\"
            r"\ast & \ast & \cdots & 1 \end{bmatrix}"
        )

        label_L = MathTex("L")
        group_L = VGroup(label_L, L).arrange(DOWN)

        #L^T (upper triangular)
        LT = MathTex(
            r"\begin{bmatrix} 1 & * & \cdots & * \\"
            r"0 & 1 & \cdots & * \\"
            r"\vdots & \vdots & \ddots & \vdots \\"
            r"0 & 0 & \cdots & 1 \end{bmatrix}"
        )

        label_LT = MathTex("L^T")
        group_LT = VGroup(label_LT, LT).arrange(DOWN)

         #Layout cuối cùng
        full_expr = VGroup(group_A, eq, group_L, group_LT).arrange(RIGHT, buff=1)
        group_LT.next_to(group_L, RIGHT, buff=0.4)
        full_expr.scale(0.7)
        full_expr.move_to(ORIGIN)

         # 1. A xuất hiện ở giữa
        self.play(FadeIn(group_A, shift=UP), run_time=1.2)
        self.wait()

        # 3. hiện dấu =
        eq.move_to(full_expr[1])
        self.play(FadeIn(eq, shift=UP))

        # 4. hiện L
        group_L.move_to(full_expr[2])
        self.play(FadeIn(group_L, shift=UP))

        # 5. hiện L^T
        group_LT.move_to(full_expr[3])
        self.play(FadeIn(group_LT, shift=UP))

        self.wait()

class Steps(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        # Title
        title = Text("Finding Cholesky Decomposition", font_size=40)
        title.to_edge(UP)

        line = Line(LEFT*5, RIGHT*5).next_to(title, DOWN)

        self.play(Write(title), Create(line))
        self.wait()

        # STEP 1: l11
        step1 = MathTex(r"(i)\ \text{Compute diagonal elements}")
        step1.set_color(BLUE)
        step1.next_to(line, DOWN, buff=0.8)
        step1.align_to(line, LEFT)

        formula1 = MathTex(
            r"l_{jj} = \sqrt{a_{jj} - \sum_{k=0}^{j-1} l_{jk}^2}"
        )
        formula1.next_to(step1, DOWN)
        formula1.align_to(step1, LEFT)

        self.play(Write(step1))
        self.play(Write(formula1))
        self.wait()

        self.play(step1.animate.set_color(WHITE), FadeOut(formula1))

        # STEP 2: l21
        step2 = MathTex(r"(ii)\ \text{Compute off-diagonal elements}")
        step2.set_color(BLUE)
        step2.next_to(step1, DOWN)
        step2.align_to(step1, LEFT)

        formula2 = MathTex(
            r"l_{ij} = \frac{a_{ij} - \sum_{k=0}^{j-1} l_{ik}l_{jk}}{l_{jj}}"
        )
        formula2.next_to(step2, DOWN)
        formula2.align_to(step2, LEFT)

        self.play(Write(step2))
        self.play(Write(formula2))
        self.wait()

        self.play(step2.animate.set_color(WHITE), FadeOut(formula2))

        # STEP 3: l22
        step3 = MathTex(r"(iii)\ \text{Repeat for all columns } j = 1 \to n")
        step3.set_color(BLUE)
        step3.next_to(step2, DOWN)
        step3.align_to(step2, LEFT)

        self.play(Write(step3))
        self.wait()

        self.play(step3.animate.set_color(WHITE))

        # FINAL RESULT
        result = MathTex(r"A = LL^T")
        result.scale(1.5)
        result.set_color(GREEN)
        result.move_to(DOWN*1.5)
        self.play(Write(result))
        self.wait()

class CholeskyStep1(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        title = Text("Step 1: Compute first diagonal element", font_size=36)
        title.to_edge(UP)
        line = Line(LEFT*5, RIGHT*5).next_to(title, DOWN)

        self.play(Write(title), Create(line))

        step = MathTex(r"(i)\ l_{11} = \sqrt{a_{11}}")
        step.set_color(BLUE)
        step.next_to(line, DOWN, buff=0.8)
        step.align_to(line, LEFT)

        self.play(Write(step))

        # Matrix A
        A = Matrix([
            [4, 2, 2],
            [2, 5, 1],
            [2, 1, 3]
        ])

        L = Matrix([
            ["?", "0", "0"],
            ["?", "?", "0"], 
            ["?", "?", "?"]
        ])

   
        group = VGroup(A, L).arrange(RIGHT, buff=2)
        group.move_to(ORIGIN).shift(DOWN*0.5)

        # label
        label_A = MathTex("A").next_to(A, UP)
        label_L = MathTex("L").next_to(L, UP)

        self.play(Write(A), FadeIn(L))
        self.play(Write(label_A), Write(label_L))
        self.wait()

        entries = A.get_entries()
        
        # highlight a11
        self.play(entries[0].animate.set_color(RED))
        self.wait()

        # tính toán
        calc = MathTex(r"l_{11} = \sqrt{4} = 2")
        calc.move_to(DOWN*2.6)

        self.play(Write(calc))
        self.wait()

        L_entries = L.get_entries()

        result_number = calc[-1]

        self.play(calc.animate.set_color(YELLOW))
        self.wait(0.3)

        # copy toàn bộ công thức
        flying_expr = calc.copy()

        # bay + co lại thành 1 điểm (ô L[0][0])
        self.play(
            flying_expr.animate.scale(0.3).move_to(L_entries[0]),
            run_time=0.8
        )
        # biến thành số 2
        new_two = MathTex("2").move_to(L_entries[0])

        self.play(
            Transform(flying_expr, new_two)
        )
        self.remove(L_entries[0])
        self.add(new_two)

        # highlight
        self.play(new_two.animate.set_color(GREEN))
        self.wait()

class CholeskyStep2(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        # TITLE
        title = Text("Step 2: Compute first column", font_size=36)
        title.to_edge(UP)
        line = Line(LEFT*5, RIGHT*5).next_to(title, DOWN)

        self.play(Write(title), Create(line))

        # STEP
        step = MathTex(r"(ii)\ l_{i1} = \frac{a_{i1}}{l_{11}}")
        step.set_color(BLUE)
        step.next_to(line, DOWN, buff=0.4)
        step.align_to(line, LEFT)

        self.play(Write(step))

        # MATRIX
        A = Matrix([
            [4, 2, 2],
            [2, 5, 1],
            [2, 1, 3]
        ])

        L = Matrix([
            ["2", "0", "0"],
            ["?", "?", "0"], 
            ["?", "?", "?"]
        ])
        # group layout 
        group = VGroup(A, L).arrange(RIGHT, buff=2)
        group.move_to(ORIGIN).shift(DOWN*0.5)

        # label (sau khi đã set vị trí)
        label_A = MathTex("A").next_to(A, UP)
        label_L = MathTex("L").next_to(L, UP)

        self.play(Write(A), FadeIn(L))
        self.play(Write(label_A), Write(label_L))
        self.wait()

        entries = A.get_entries()
        L_entries = L.get_entries()

        # highlight a21 & a31 
        self.play(
            entries[3].animate.set_color(RED),  # a21
            entries[6].animate.set_color(RED)   # a31
        )
        self.wait()

        # calc
        calc1 = MathTex(r"l_{21} = \frac{2}{2} = 1")
        calc2 = MathTex(r"l_{31} = \frac{2}{2} = 1")

        calc_group = VGroup(calc1, calc2).arrange(RIGHT, buff=2)
        calc_group.next_to(group, DOWN, buff=0.8)

        self.play(Write(calc_group))
        self.wait()

        # highlight công thức
        self.play(calc1.animate.set_color(YELLOW), calc2.animate.set_color(YELLOW))
        self.wait(0.3)

        # copy nguyên công thức
        fly1 = calc1.copy()
        fly2 = calc2.copy()

        # bay + co lại
        self.play(
            fly1.animate.scale(0.3).move_to(L_entries[3]),
            fly2.animate.scale(0.3).move_to(L_entries[6]),
            run_time=0.8
        )

        # biến thành số 1
        new1 = MathTex("1").move_to(L_entries[3])
        new2 = MathTex("1").move_to(L_entries[6])

        self.play(
            Transform(fly1, new1),
            Transform(fly2, new2)
        )
        # thay ? bằng 1
        self.remove(L_entries[3], L_entries[6])
        self.add(new1, new2)

        # highlight
        self.play(
            new1.animate.set_color(GREEN),
            new2.animate.set_color(GREEN)
        )

class CholeskyStep3(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        # TITLE
        title = Text("Step 3: Compute next diagonal element", font_size=36)
        title.to_edge(UP)
        line = Line(LEFT*5, RIGHT*5).next_to(title, DOWN)

        self.play(Write(title), Create(line))

        # STEP
        step = MathTex(r"(iii)\ l_{jj} = \sqrt{a_{jj} - \sum_{k=1}^{j-1} l_{jk}^2}")
        step.set_color(BLUE)
        step.next_to(line, DOWN, buff=0.4)
        step.align_to(line, LEFT)

        self.play(Write(step))

        # MATRIX
        A = Matrix([
            [4, 2, 2],
            [2, 5, 1],
            [2, 1, 3]
        ])

        L = Matrix([
            ["2", "0", "0"],
            ["1", "?", "0"], 
            ["1", "?", "?"]
        ])

        group = VGroup(A, L).arrange(RIGHT, buff=2)
        group.move_to(ORIGIN).shift(DOWN*1.2)

        label_A = MathTex("A").next_to(A, UP)
        label_L = MathTex("L").next_to(L, UP)

        self.play(Write(A), FadeIn(L))
        self.play(Write(label_A), Write(label_L))
        self.wait()

        entries = A.get_entries()
        L_entries = L.get_entries()

        # highlight a22 & l21
        self.play(
            entries[4].animate.set_color(RED),   # a22
            L_entries[3].animate.set_color(YELLOW)  # l21
        )
        self.wait()

        # calc
        calc = MathTex(r"l_{22} = \sqrt{5 - 1^2} = 2")
        calc.next_to(group, DOWN, buff=0.4)
        calc.move_to([0, calc.get_y(), 0])

        self.play(Write(calc))
        self.wait()

        # highlight formula
        self.play(calc.animate.set_color(YELLOW))
        self.wait(0.3)

        # bay công thức
        fly = calc.copy()

        self.play(
            fly.animate.scale(0.3).move_to(L_entries[4]),
            run_time=0.8
        )

        # transform thành số 2
        new2 = MathTex("2").move_to(L_entries[4])

        self.play(Transform(fly, new2))

        # thay ? bằng 2
        self.remove(L_entries[4])
        self.add(new2)

        # highlight
        self.play(new2.animate.set_color(GREEN))
        self.wait()

class CholeskyStep4(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        # TITLE
        title = Text("Step 4: Compute off-diagonal element", font_size=36)
        title.to_edge(UP)
        line = Line(LEFT*5, RIGHT*5).next_to(title, DOWN)

        self.play(Write(title), Create(line))

        # STEP
        step = MathTex(r"(iv)\ l_{ij} = \frac{a_{ij} - \sum l_{ik}l_{jk}}{l_{jj}}")
        step.set_color(BLUE)
        step.next_to(line, DOWN, buff=0.4)
        step.align_to(line, LEFT)

        self.play(Write(step))

        # MATRIX
        A = Matrix([
            [4, 2, 2],
            [2, 5, 1],
            [2, 1, 3]
        ])

        L = Matrix([
            ["2", "0", "0"],
            ["1", "2", "0"], 
            ["1", "?", "?"]
        ])

        group = VGroup(A, L).arrange(RIGHT, buff=2)
        group.move_to(ORIGIN).shift(DOWN*0.7)

        label_A = MathTex("A").next_to(A, UP)
        label_L = MathTex("L").next_to(L, UP)

        self.play(Write(A), FadeIn(L))
        self.play(Write(label_A), Write(label_L))
        self.wait()

        entries = A.get_entries()
        L_entries = L.get_entries()

        # highlight a32, l31, l21
        self.play(
            entries[7].animate.set_color(RED),      # a32
            L_entries[6].animate.set_color(YELLOW), # l31
            L_entries[3].animate.set_color(YELLOW)  # l21
        )
        self.wait()

        # calc
        calc = MathTex(r"l_{32} = \frac{1 - 1\cdot1}{2} = 0")
        calc.next_to(group, DOWN, buff=0.8)
        calc.move_to([0, calc.get_y(), 0])

        self.play(Write(calc))
        self.wait()

        # highlight formula
        self.play(calc.animate.set_color(YELLOW))
        self.wait(0.3)

        # công thức
        fly = calc.copy()

        self.play(
            fly.animate.scale(0.3).move_to(L_entries[7]),
            run_time=0.8
        )

        # transform thành 0
        new0 = MathTex("0").move_to(L_entries[7])

        self.play(Transform(fly, new0))

        # thay ? bằng 0
        self.remove(L_entries[7])
        self.add(new0)

        # highlight
        self.play(new0.animate.set_color(GREEN))
        self.wait()

class CholeskyStep5(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        # TITLE
        title = Text("Step 5: Compute final diagonal element", font_size=36)
        title.to_edge(UP)
        line = Line(LEFT*5, RIGHT*5).next_to(title, DOWN)

        self.play(Write(title), Create(line))

        # STEP
        step = MathTex(r"(v)\ l_{jj} = \sqrt{a_{jj} - \sum l_{jk}^2}")
        step.set_color(BLUE)
        step.next_to(line, DOWN, buff=0.4)
        step.align_to(line, LEFT)

        self.play(Write(step))

        # MATRIX
        A = Matrix([
            [4, 2, 2],
            [2, 5, 1],
            [2, 1, 3]
        ])

        L = Matrix([
            ["2", "0", "0"],
            ["1", "2", "0"], 
            ["1", "0", "?"]
        ])

        group = VGroup(A, L).arrange(RIGHT, buff=2)
        group.move_to(ORIGIN).shift(DOWN*0.5)

        label_A = MathTex("A").next_to(A, UP)
        label_L = MathTex("L").next_to(L, UP)

        self.play(Write(A), FadeIn(L))
        self.play(Write(label_A), Write(label_L))
        self.wait()

        entries = A.get_entries()
        L_entries = L.get_entries()

        # highlight a33, l31, l32
        self.play(
            entries[8].animate.set_color(RED),      # a33
            L_entries[6].animate.set_color(YELLOW), # l31
            L_entries[7].animate.set_color(YELLOW)  # l32
        )
        self.wait()

        # calc
        calc = MathTex(r"l_{33} = \sqrt{3 - (1^2 + 0^2)} = \sqrt{2}")
        calc.next_to(group, DOWN, buff=1)
        calc.move_to([0, calc.get_y(), 0])

        self.play(Write(calc))
        self.wait()

        # highlight
        self.play(calc.animate.set_color(YELLOW))
        self.wait(0.3)

        # bay công thức
        fly = calc.copy()

        self.play(
            fly.animate.scale(0.3).move_to(L_entries[8]),
            run_time=0.8
        )

        # transform thành sqrt(2)
        new_val = MathTex(r"\sqrt{2}").move_to(L_entries[8])

        self.play(Transform(fly, new_val))

        # thay ? bằng sqrt(2)
        self.remove(L_entries[8])
        self.add(new_val)

        # highlight
        self.play(new_val.animate.set_color(GREEN))
        self.wait()

class Result(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        # TITLE
        title = Text("Final Result: Cholesky Decomposition", font_size=34)
        title.to_edge(UP)
        self.play(Write(title))

        # MATRIX A
        A = Matrix([
            [4, 2, 2],
            [2, 5, 1],
            [2, 1, 3]
        ])

        label_A = MathTex("A")
        group_A = VGroup(label_A, A).arrange(DOWN, buff=0.2)

        # MATRIX L
        L = Matrix([
            ["2", "0", "0"],
            ["1", "2", "0"],
            ["1", "0", r"\sqrt{2}"]
        ])

        label_L = MathTex("L")
        group_L = VGroup(label_L, L).arrange(DOWN, buff=0.2)

        # MATRIX LT 
        LT = Matrix([
            ["2", "1", "1"],
            ["0", "2", "0"],
            ["0", "0", r"\sqrt{2}"]
        ])

        label_LT = MathTex("L^T")
        group_LT = VGroup(label_LT, LT).arrange(DOWN, buff=0.2)

        # dấu = 
        eq = MathTex("=")

        # layout tổng
        group_L_LT = VGroup(group_L, group_LT).arrange(RIGHT, buff=0.4)

        full_expr = VGroup(group_A, eq, group_L_LT).arrange(RIGHT, buff=0.8)
        full_expr.scale(0.75)  # 👈 quan trọng: scale nhỏ lại
        full_expr.move_to(ORIGIN).shift(DOWN*0.3)

        # animation

        # 1. hiện A
        self.play(FadeIn(group_A, shift=UP))
        self.wait(0.3)

        # 2. hiện =
        self.play(Write(eq))
        self.wait(0.3)

        # 3. hiện L
        self.play(FadeIn(group_L, shift=UP))
        self.wait(0.5)
        self.play(Write(label_LT))
        self.wait(0.5)

        # 4. BIẾN L → L^T 
         # copy L
        LT_copy = L.copy()
        LT_copy.move_to(group_LT[1])

        self.play(FadeIn(LT_copy))
        self.wait()

        L_entries = LT_copy.get_entries()
        n = 3

        animations = []

        for i in range(n):
            for j in range(i+1, n):
                idx1 = i*n + j
                idx2 = j*n + i

                a = L_entries[idx1]
                b = L_entries[idx2]

                animations.append(
                    a.animate.move_to(b.get_center()).set_path_arc(PI/2)
                )
                animations.append(
                    b.animate.move_to(a.get_center()).set_path_arc(PI/2)
                )

        self.play(*animations, run_time=1.5)
        self.wait()

        # highlight
        box = SurroundingRectangle(full_expr, color=YELLOW)
        self.play(Create(box))

        final_text = MathTex(r"A = LL^T").set_color(YELLOW)
        final_text.next_to(full_expr, DOWN)

        self.play(Write(final_text))
        self.wait()

class DiagonalStep1Eigenvalues(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        # TITLE 
        title = Text("Diagonalization: Eigenvalues", font_size=36)
        title.to_edge(UP)

        line = Line(LEFT*5, RIGHT*5).next_to(title, DOWN)

        self.play(Write(title), Create(line))

        # MATRIX A 
        A = Matrix([
            [4, 2, 2],
            [2, 5, 1],
            [2, 1, 3]
        ])

        A.move_to(ORIGIN).shift(LEFT*2 + DOWN*0.5)

        label_A = MathTex("A").next_to(A, UP)

        self.play(Write(A), Write(label_A))
        self.wait()

        # STEP TEXT
        step = MathTex(r"\det(A - \lambda I) = 0")
        step.set_color(BLUE)
        step.next_to(line, DOWN, buff=0.4)
        step.align_to(line, LEFT)

        self.play(Write(step))
        self.wait()

        # highlight A
        self.play(A.animate.set_color(RED))
        self.wait()

        # characteristic polynomial
        poly = MathTex(r"\Rightarrow \lambda^3 - 12\lambda^2 + 39\lambda - 36 = 0")
        poly.next_to(A, DOWN, buff=1)

        self.play(Write(poly))
        self.wait()
        self.play(A.animate.set_color(WHITE))
        # eigenvalues
        eig1 = MathTex(r"\lambda_1 = 6")
        eig2 = MathTex(r"\lambda_2 = \lambda_3 = 3")

        eig_group = VGroup(eig1, eig2).arrange(DOWN, aligned_edge=LEFT)
        eig_group.next_to(A, RIGHT, buff=2)

        # transform từ poly → eigenvalues
        self.play(
            TransformFromCopy(poly, eig_group),
            run_time=1.2
        )
        self.wait()

        # highlight từng eigenvalue 
        self.play(eig1.animate.set_color(YELLOW))
        self.wait(0.3)

        self.play(eig2.animate.set_color(YELLOW))
        self.wait(0.3)
        
        # reset màu cho đẹp
        self.play(
            eig_group.animate.set_color(WHITE),
            A.animate.set_color(WHITE)
        )

        self.wait()

class DiagonalStep2Eigenvectors(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        # TITLE
        title = Text("Diagonalization: Eigenvectors", font_size=36)
        title.to_edge(UP)

        line = Line(LEFT*5, RIGHT*5).next_to(title, DOWN)

        self.play(Write(title), Create(line))

        #STEP
        step = MathTex(r"(A - \lambda I)x = 0")
        step.set_color(BLUE)
        step.next_to(line, DOWN, buff=0.4)
        step.align_to(line, LEFT)

        self.play(Write(step))

        #MATRIX A
        A = Matrix([
            [4, 2, 2],
            [2, 5, 1],
            [2, 1, 3]
        ])

        A.move_to(ORIGIN).shift(LEFT*3 + DOWN*0.5)
        label_A = MathTex("A").next_to(A, UP)

        self.play(Write(A), Write(label_A))

        # eigenvalues
        eig1 = MathTex(r"\lambda_1 = 6")
        eig2 = MathTex(r"\lambda_2 = \lambda_3 = 3")

        eig_group = VGroup(eig1, eig2).arrange(DOWN, aligned_edge=LEFT)
        eig_group.next_to(A, RIGHT, buff=1).shift(LEFT*0.5 + UP*0.3)

        self.play(Write(eig_group))
        self.wait()

        # eigenvectors
        v1 = MathTex(r"v_1 = \begin{bmatrix}1 \\ 1 \\ 1\end{bmatrix}")
        v2 = MathTex(r"v_2 = \begin{bmatrix}1 \\ -1 \\ 0\end{bmatrix}")
        v3 = MathTex(r"v_3 = \begin{bmatrix}1 \\ 0 \\ -1\end{bmatrix}")
        v1.scale(0.8)
        v2.scale(0.8)
        v3.scale(0.8)

        # chia riêng từng vector
        # anchor bên phải lambda
        anchor = eig_group.get_right() + RIGHT*1.5

        # v1 ở trên
        v1.move_to(anchor + UP*1.2)

        # v2 bên trái dưới
        v2.move_to(anchor + DOWN*0.8 + LEFT*0.8)

        # v3 bên phải dưới
        v3.move_to(anchor + DOWN*0.8 + RIGHT*1.4)

        # group lại cho dễ control
        v_group = VGroup(v1, v2, v3)
        v_group.shift(RIGHT*0.5 + DOWN*0.6) 


        # λ1 → v1
        expr1 = MathTex(r"A - 6I")
        expr1.next_to(VGroup(A, eig_group, v_group), DOWN)
        expr1.move_to(expr1.get_center()[1]*UP + ORIGIN[0]*RIGHT)
        expr1.align_to(ORIGIN, LEFT)

        self.play(
            eig1.animate.set_color(YELLOW),
            A.animate.set_color(RED)
        )

        self.play(Write(expr1))
        self.play(expr1.animate.set_color(GREEN))

        self.play(
            TransformFromCopy(expr1, v1),
            run_time=0.8
        )

        self.play(FadeOut(expr1))
        self.wait(0.3)

        # reset A
        self.play(A.animate.set_color(WHITE))

        # λ2 → v2, v3
        expr2 = MathTex(r"A - 3I")
        expr2.move_to(expr1)

        self.play(
            eig2.animate.set_color(YELLOW),
            A.animate.set_color(RED)
        )

        self.play(Write(expr2))
        self.play(expr2.animate.set_color(GREEN))

        self.play(
            TransformFromCopy(expr2, v2),
            TransformFromCopy(expr2, v3),
            run_time=1
        )

        self.play(FadeOut(expr2))
        self.wait()

        # reset màu
        self.play(
            eig_group.animate.set_color(WHITE),
            v_group.animate.set_color(WHITE),
            A.animate.set_color(WHITE)
        )

        self.wait()\

class DiagonalStep3PandD(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        # TITLE
        title = Text("Construct Matrices P and D", font_size=36)
        title.to_edge(UP)

        line = Line(LEFT*5, RIGHT*5).next_to(title, DOWN)

        self.play(Write(title), Create(line))

        # eigenvectors
        v1 = MathTex(r"\begin{bmatrix}1 \\ 1 \\ 1\end{bmatrix}")
        v2 = MathTex(r"\begin{bmatrix}1 \\ -1 \\ 0\end{bmatrix}")
        v3 = MathTex(r"\begin{bmatrix}1 \\ 0 \\ -1\end{bmatrix}")

        v_group = VGroup(v1, v2, v3).arrange(RIGHT, buff=1.5)
        v_group.set_color(WHITE)
        v_group.move_to(UP*1)
        vectors = [v1, v2, v3]

        self.play(Write(v_group))
        self.wait()

        # eigenvalues
        l1 = MathTex("6")
        l2 = MathTex("3")
        l3 = MathTex("3")

        lambda_group = VGroup(l1, l2, l3).arrange(RIGHT, buff=1.5)
        lambda_group.set_color(WHITE)
        lambda_group.next_to(v_group, DOWN, buff=1)

        self.play(Write(lambda_group))
        self.wait()

        # MATRIX P
        P = Matrix([
            ["?", "?", "?"],
            ["?", "?", "?"],
            ["?", "?", "?"]
        ])
        P.set_color(WHITE)

        label_P = MathTex("P")
        group_P = VGroup(label_P, P).arrange(DOWN)
        group_P.to_edge(LEFT).shift(DOWN*0.5)

        self.play(FadeIn(group_P))
        self.wait()

        # MATRIX D
        D = Matrix([
            ["?", "0", "0"],
            ["0", "?", "0"],
            ["0", "0", "?"]
        ])
        D.set_color(WHITE)
        

        label_D = MathTex("D")
        group_D = VGroup(label_D, D).arrange(DOWN)
        group_D.to_edge(RIGHT).shift(DOWN*0.5)

        self.play(FadeIn(group_D))
        self.wait()

        # FILL P 
        P_entries = P.get_entries()

        values = [
            ["1","1","1"],
            ["1","-1","0"],
            ["1","0","-1"]
        ]

        for i in range(3):
            vec = vectors[i]

            #self.play(vec.animate.set_color(YELLOW))

            for j in range(3):
                idx = j*3 + i
                target = P_entries[idx]

                flying = MathTex(values[i][j]).set_color(YELLOW)
                flying.move_to(vec.get_center())

                # bay + co lại vào ô
                self.play(
                    flying.animate.scale(0.5).move_to(target),
                    run_time=0.5
                )

                #tạo số mới
                new_val = MathTex(values[i][j]).set_color(YELLOW).move_to(target)

                # biến thành số
                self.play(
                    Transform(flying, new_val),
                    run_time=0.3
                )

                # thay dấu ?
                self.remove(target)
                self.add(new_val)
                #self.play(FadeOut(vec))
            self.play(FadeOut(vec))


        # FILL D 
        
        D_entries = D.get_entries()
        lambdas = [l1, l2, l3]
        lambda_vals = ["6","3","3"]
        diag_indices = [0, 4, 8]

        for i in range(3):
            lam = lambdas[i]
            target = D_entries[diag_indices[i]]

            self.play(lam.animate.set_color(GREEN))

            flying = lam.copy()

            # bay vào ô
            self.play(
                flying.animate.scale(0.5).move_to(target),
                run_time=0.3
            )

            # tạo giá trị mới
            new_val = MathTex(lambda_vals[i]).set_color(GREEN).move_to(target)

            # biến thành số
            self.play(
                Transform(flying, new_val),
                run_time=0.3
            )

            # thay dấu ?
            self.remove(target)
            self.add(new_val)

            self.play(FadeOut(lam))
        self.wait(0.5)

class DiagonalStep4Final(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        # TITLE 
        title = Text("Final: Diagonalization", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))

        # MATRIX A 
        A = Matrix([
            [4, 2, 2],
            [2, 5, 1],
            [2, 1, 3]
        ])
        label_A = MathTex("A")
        group_A = VGroup(label_A, A).arrange(DOWN)

        # MATRIX P 
        P = Matrix([
            ["1","1","1"],
            ["1","-1","0"],
            ["1","0","-1"]
        ])
        label_P = MathTex("P")
        group_P = VGroup(label_P, P).arrange(DOWN)

        # MATRIX D 
        D = Matrix([
            ["6","0","0"],
            ["0","3","0"],
            ["0","0","3"]
        ])
        label_D = MathTex("D")
        group_D = VGroup(label_D, D).arrange(DOWN)

        # MATRIX P^-1 
        Pinv = Matrix([
            ["1/3", "1/3", "1/3"],
            ["1/2", "-1/2", "0"],
            ["1/2", "0", "-1/2"]
        ])
        label_Pinv = MathTex("P^{-1}")
        group_Pinv = VGroup(label_Pinv, Pinv).arrange(DOWN)

        # dấu = 
        eq = MathTex("=")

        # layout 
        full = VGroup(
            group_A, eq, group_P, group_D, group_Pinv
        ).arrange(RIGHT, buff=0.5)

        full.scale(0.65) 
        full.move_to(ORIGIN).shift(DOWN*0.3)

        # animation 

        # 1. hiện A
        self.play(FadeIn(group_A, shift=UP))
        self.wait(0.3)

        # 2. hiện =
        self.play(Write(eq))
        self.wait(0.3)

        # 3. hiện P
        self.play(FadeIn(group_P, shift=UP))
        self.wait(0.3)

        # 4. hiện D
        self.play(FadeIn(group_D, shift=UP))
        self.wait(0.3)

        # tạo P^-1 từ P
        P_copy = group_P.copy()

        # copy xuất hiện
        self.play(
            TransformFromCopy(group_P, P_copy),
            run_time=0.8
        )

        # bay sang phải
        self.play(
            P_copy.animate.move_to(group_Pinv.get_center()),
            run_time=0.6
        )

        # xoay nhẹ 
        self.play(
            P_copy.animate.scale(0.9).rotate(PI),
            run_time=0.5
        )

        # biến thành ma trận P^-1 
        self.play(
            Transform(P_copy, group_Pinv),
            run_time=0.7
        )

        self.wait(0.5)

        # highlight 
        box = SurroundingRectangle(full, color=YELLOW)
        self.play(Create(box))

        final_text = MathTex(r"A = P D P^{-1}").set_color(YELLOW)
        final_text.next_to(full, DOWN)

        self.play(Write(final_text))
        self.wait()