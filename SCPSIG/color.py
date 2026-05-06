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


### Color constants ###

# Transparent pixel (alongside a transparency scale)
TRANSPARENT = Color(255, 255, 255, 0)

TRANSPARENT_100 = TRANSPARENT
TRANSPARENT_75 = Color(255, 255, 255, 64)
TRANSPARENT_50 = Color(255, 255, 255, 127)
TRANSPARENT_25 = Color(255, 255, 255, 191)

# Monochrome scales
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
GRAY = Color(127, 127, 127)

SHADE_0 = BLACK
SHADE_25 = Color(64, 64, 64)
SHADE_50 = GRAY
SHADE_75 = Color(191, 191, 191)
SHADE_100 = WHITE

# RGB & CMY primitives
RED = Color(255, 0, 0)
GREEN = Color(0, 255, 0)
BLUE = Color(0, 0, 255)

MAGENTA = Color(255, 0, 255)
CYAN = Color(0, 255, 255)
YELLOW = Color(255, 255, 0)

# Other known colors
