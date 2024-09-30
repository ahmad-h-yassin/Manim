from manim import *

class CartesianPlaneAndVectors(Scene):
    def construct(self):
        # Create axes
        axes = Axes(
            x_range=(-5, 5, 1),
            y_range=(-5, 5, 1),
            axis_config={"color": BLUE},
        )

        # Label x and y axes
        axes_labels = axes.get_axis_labels("x", "y")

        # Create vectors
        i_vector = Vector(direction=RIGHT, color=RED)
        j_vector = Vector(direction=UP, color=GREEN)

        # Create labels for vectors
        i_label = Tex(r"\hat{i}", color=RED).next_to(i_vector, RIGHT)
        j_label = Tex(r"\hat{j}", color=GREEN).next_to(j_vector, UP)

        # Fade in axes and labels
        self.play(Create(axes), Write(axes_labels))

        # Fade in vectors and labels
        self.play(Create(i_vector), Write(i_label))
        self.play(Create(j_vector), Write(j_label))

        self.wait(1)
