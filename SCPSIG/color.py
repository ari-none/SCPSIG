from __future__ import annotations


### The color class ###
class Color:
    """
    The color class used for drawing images.
    """
    
    def __init__(self, r: int | float, g: int | float, b: int | float, a: int | float = 255):
        """
        Creates a color following the RGBA (or RGB) coloring convention.
        :param r: The red value.
        :param g: The green value.
        :param b: The blue value.
        :param a: The alpha value. (set to 255 by default, which is completely opaque)
        """
        
        self.r: int = round(max(0, min(r, 255)))
        self.g: int = round(max(0, min(g, 255)))
        self.b: int = round(max(0, min(b, 255)))
        self.a: int = round(max(0, min(a, 255)))
    
    def __add__(self, other: Color):
        return Color(
            self.r + other.r,
            self.g + other.g,
            self.b + other.b,
            self.a + other.a
        )

    def __sub__(self, other: Color):
        return Color(
            self.r - other.r,
            self.g - other.g,
            self.b - other.b,
            self.a - other.a
        )

    def __mul__(self, other: Color | float) -> Color:
        if isinstance(other, Color):
            return Color(
                round(self.r * other.r / 255),
                round(self.g * other.g / 255),
                round(self.b * other.b / 255),
                round(self.a * other.a / 255)
            )
        return Color(
            round(self.r * other),
            round(self.g * other),
            round(self.b * other),
            round(self.a * other)
        )
    
    def __truediv__(self, other: Color):
        return Color(
            round(self.r / other.r),
            round(self.g / other.g),
            round(self.b / other.b),
            round(self.a / other.a)
        )

    def __eq__(self, other: Color) -> bool:
        return (
            self.r == other.r and
            self.g == other.g and
            self.b == other.b and
            self.a == other.a
        )
    
    def __str__(self) -> str:
        return f"#{hex(self.r)}{hex(self.g)}{hex(self.b)}{hex(self.a)}"
    
    def __repr__(self) -> str:
        return f"Color({self.r}, {self.g}, {self.b}, {self.a})"
    
    def __neg__(self) -> Color:
        return Color(
            255 - self.r,
            255 - self.g,
            255 - self.b,
        )

    ### Static methods for the class ###
    
    @staticmethod
    def vector(r: float, g: float, b: float, a: float = 1):
        """
        Creates a color following the color vertex convention. (aka: each color is a value between 0 and 1)
        :param r: The red value.
        :param g: The green value.
        :param b: The blue value.
        :param a: The alpha value. (set to 1 by default, which is completely opaque)
        :return: 
        """
        return Color(
            r * 255,
            g * 255,
            b * 255,
            a * 255
        )

    @staticmethod
    def lerp(start: Color, end: Color, alpha: float) -> Color:
        """
        Returns a color within the linear interpolation of two colors.
        :param start: The initial color.
        :param end: The target color.
        :param alpha: The alpha interpolation value, between 0.0 and 1.0. (0.0 returns the initial color, 1.0 returns the target color)
        :return: The interpolated color.
        """
        return Color(
            start.r * (1 - alpha) + end.r * alpha,
            start.g * (1 - alpha) + end.g * alpha,
            start.b * (1 - alpha) + end.b * alpha,
            start.a * (1 - alpha) + end.a * alpha
        )