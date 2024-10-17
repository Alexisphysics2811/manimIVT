from manim import *
from manim.utils.color.XKCD import BROWNISH


class GeneralizedIVT_es(Scene):
    def construct(self):
        # Title in LaTeX
        title = Tex(r"Teorema de Valor Intermedio para $\mathbb{R}^n$").to_edge(UP)
        self.play(Write(title))

        # A as a connected region in R^n (represented in 2D for visualization)
        A_text = Tex(r"Sea $A \subseteq \mathbb{R}^n$ conexo").scale(0.5).next_to(title, DOWN)
        self.play(Write(A_text))
        self.wait(1)

        A_shape = Ellipse(width=3.5, height=2, color=BLUE, fill_opacity=0.3)
        A_label = MathTex(r"A \subseteq \mathbb{R}^n").next_to(A_shape, UP)
        self.play(Create(A_shape), Write(A_label))
        self.wait(1)
        self.play(FadeOut(A_text))

        # Points in A (x1 and x2) with LaTeX labels
        x_points_text = Tex(r"Tome cualesquiera $x_1,x_2 \in A$ distintos").scale(0.5).next_to(title, DOWN)
        self.play(Write(x_points_text))
        self.wait(1)
        point_x1 = Dot(A_shape.get_center() + 0.5 * LEFT + 0.3 * UP, color=RED)
        point_x2 = Dot(A_shape.get_center() + 0.6 * RIGHT + 0.4 * DOWN, color=RED)
        label_x1 = MathTex(r"x_1").next_to(point_x1, LEFT)
        label_x2 = MathTex(r"x_2").next_to(point_x2, RIGHT)
        self.play(FadeIn(point_x1, label_x1), FadeIn(point_x2, label_x2))
        self.wait(1)
        self.play(FadeOut(x_points_text))

        # Moving the entire set A (with points) to the left
        self.play(A_shape.animate.shift(LEFT * 2),
                  A_label.animate.shift(LEFT * 2),
                  point_x1.animate.shift(LEFT * 2),
                  point_x2.animate.shift(LEFT * 2),
                  label_x1.animate.shift(LEFT * 2),
                  label_x2.animate.shift(LEFT * 2),)

        # Mapping f(A) as a connected set in R
        # Represented as a vertical line (f(A) subset of R)
        f_A_text = Tex(r"$f(A)$ es conexo y subconjunto de $\mathbb{R}$, así que es un intervalo").scale(0.5).next_to(title, DOWN)
        self.play(Write(f_A_text))
        self.wait(1)
        f_A_line = NumberLine(
            x_range=[-2, 2, 0.5],  # Tick marks every 0.5
            length=4,
            color=YELLOW,
            include_numbers=False,  # Show numbers for each tick
            rotation=PI / 2  # Make it vertical
        ).shift(RIGHT * 3)
        f_A_label = MathTex(r"f(A) \subseteq \mathbb{R}").next_to(f_A_line, RIGHT)

        self.play(Create(f_A_line), Write(f_A_label))
        self.wait(1)
        self.play(FadeOut(f_A_text))

        # f(x1) and f(x2) points in R
        f_x_text = Tex(r"Entonces para $f(x_1), f(x_2) \in f(A)$ tenemos que $f(x_1)<f(x_2)$ sin pérdida de generalidad").scale(0.5).next_to(title, DOWN)
        self.play(Write(f_x_text))
        self.wait(1)
        f_x1_point = point_x1.copy()
        f_x2_point = point_x2.copy()

        self.play(
            Transform(f_x1_point, Dot(f_A_line.n2p(-1.5), color=GREEN)),
            Transform(f_x2_point, Dot(f_A_line.n2p(1.5), color=GREEN))
        )

        f_x1_label = MathTex(r"f(x_1)").next_to(f_x1_point, LEFT)
        f_x2_label = MathTex(r"f(x_2)").next_to(f_x2_point, LEFT)

        self.play(Write(f_x1_label), Write(f_x2_label))
        self.wait(1)
        self.play(FadeOut(f_x_text))

        # The intermediate value c between f(x1) and f(x2)
        c_text = Tex(r"Así, existe $c \in f(A)$ tal que $f(x_1)<c<f(x_2)$").scale(0.5).next_to(title, DOWN)
        self.play(Write(c_text))
        self.wait(1)
        c_point = Dot(f_A_line.n2p(0), color=PURPLE)
        c_label = MathTex(r"c").next_to(c_point, LEFT)

        # Move the point c up and down
        self.play(FadeIn(c_point))
        self.play(c_point.animate.shift(UP * 1.3), run_time=1)
        self.play(c_point.animate.shift(DOWN * 2.6), run_time=1)
        self.play(c_point.animate.shift(UP * 1.3), run_time=1)
        self.play(Write(c_label))
        self.wait(1)
        self.play(FadeOut(c_text))

        # Point x_c in A such that f(x_c) = c
        xc_text = Tex(r"Y como $c \in f(A)$, existe $x_c \in A$ tal que $f(x_c)=c$").scale(0.5).next_to(title, DOWN)
        self.play(Write(xc_text))
        self.wait(1)
        point_xc = Dot(A_shape.get_center() + 0.3 * RIGHT + 0.3 * UP, color=PURPLE)
        xc_label = MathTex(r"x_c").next_to(point_xc, RIGHT)

        # Make a copy of c_point before moving it to xc
        c_point_copy = c_point.copy()
        c_label_copy = c_label.copy()
        self.play(Transform(c_point_copy, point_xc),
                  Transform(c_label_copy, xc_label))

        # Use an arrow instead of a dashed line
        xc_f_c_arrow = CurvedArrow(
            start_point=point_xc.get_center() + 0.1 * RIGHT + 0.1 * DOWN,
            end_point=c_point.get_center() + 0.1 * LEFT + 0.1 * DOWN,
            color=BROWNISH,
            radius=6,  # Adjust the curvature radius
            stroke_width=2.5,  # Adjust the width of the arrow
            tip_length=0.2
        )
        arrow_label = MathTex(r"f").next_to(xc_f_c_arrow, DOWN)
        self.play(Create(xc_f_c_arrow), Write(arrow_label))
        self.wait(1)
        self.play(FadeOut(xc_text))

        # Formal theorem statement in LaTeX
        theorem_text = Tex(
            r"Por lo tanto, dada $f: A \subseteq \mathbb{R}^n \to \mathbb{R}$ continua,",
            r" y $A$ conexo,",
            r" entonces para $x_1, x_2 \in A$, si $f(x_1) < f(x_2)$,",
            r" tenemos que $\forall c \in (f(x_1), f(x_2))$,",
            r" $\exists x_c \in A$ tal que $f(x_c) = c$."
        ).scale(0.5).to_edge(DOWN)
        self.play(Write(theorem_text))

        # Hold the final scene
        self.wait(5)
