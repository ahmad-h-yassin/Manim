from manim import *

class DrawSVG(Scene):
    def construct(self):
        # Load the SVG image
        svg_path = "green-travel-svgrepo-com.svg"
        svg_image = SVGMobject(svg_path)

        # Create a rectangle border around the SVG image
        border = SurroundingRectangle(svg_image, color=WHITE, buff=SMALL_BUFF)

        # Create a filled version of the SVG image
        filled_svg_image = svg_image.copy().set_fill(GREEN, opacity=1)

        # Add the SVG image and its border to the scene
        self.add(filled_svg_image, border)

%manim -ql DrawSVG
