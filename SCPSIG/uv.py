from __future__ import annotations
from math import *


### The UV class ###
class UV:
    """
    The UV coordinates class (or just XY coordinates for shaders or something IDK)
    """
    
    # Default operations
    def __init__(self, u: float, v: float):
        """
        Creates a UV coordinate/vector.
        :param u: The horizontal axis of the UV.
        :param v: The vertical axis of the UV.
        """
        self.u: float = u
        self.v: float = v
    
    def __add__(self, other: UV) -> UV:
        return UV(self.u + other.u, self.v + other.v)
    
    def __sub__(self, other: UV) -> UV:
        return UV(self.u - other.u, self.v - other.v)
    
    def __mul__(self, other: float) -> UV:
        return UV(self.u * other, self.v * other)
    
    def __truediv__(self, other: float) -> UV:
        assert other != 0
        return UV(self.u / other, self.v / other)
    
    def __abs__(self) -> UV:
        return UV(abs(self.u), abs(self.v))
    
    def __neg__(self) -> UV:
        return UV(-self.u, -self.v)
    
    def __eq__(self, other: UV) -> bool:
        return self.u == other.u and self.v == other.v

    def __str__(self) -> str:
        return f"UV: {self.u}x{self.v}"

    def __repr__(self) -> str:
        return f"UV({self.u}, {self.v})"
    
    # Extra operations
    def normalized(self) -> UV:
        """
        Returns a normalized UV vector. (which has a length of 1)
        :return: The normalized version of the vector.
        """
        assert length(self) != 0
        return self / length(self)
    
    def centered(self) -> UV:
        """
        Returns a "centered" version of the UV (basically adds -0.5 to each coordinate). Especially useful for shader mathematics.
        :return: A centered version of the UV.
        """
        return UV(self.u - 0.5, self.v - 0.5)


### Static methods for the class ###
def length(a: UV) -> float:
    """
    Returns the length/magnitude of the vector.
    :param a: The vector.
    :return: The length/magnitude of the vector.
    """
    return sqrt(a.u**2 + a.v**2)

def dot(a: UV, b: UV) -> float:
    """
    Returns the dot product of two UV vectors.
    :param a: The first vector.
    :param b: The second vector.
    :return: The dot product.
    """
    return a.u * b.u + a.v * b.v

def cross(a: UV, b: UV) -> float:
    """
    Returns the cross product of two UV vectors.
    :param a: The first vector.
    :param b: The second vector.
    :return: The scalar of the cross product.
    """
    return a.u * b.v - a.v * b.u

def distance(a: UV, b: UV) -> float:
    """
    Returns the distance between two UV points.
    :param a: The first point.
    :param b: The second point.
    :return: The distance between both points.
    """
    return length(a - b)

def reflect(v: UV, normal: UV) -> UV:
    """Reflects vector v over a normalized normal vector."""
    return v - normal * (2 * UV.dot(v, normal))

def rotate(v: UV, angle: float) -> UV:
    """
    Rotates a UV vector.
    :param v: The vector.
    :param angle: The angle in radians.
    :return: The rotated angle.
    """
    return UV(
        v.u * cos(angle) - v.v * sin(angle),
        v.u * sin(angle) + v.v * cos(angle)
    )

def angle(v: UV) -> float:
    """
    Returns the UV vector's angle relative to the right. (positive U axis)
    :param v: The vector.
    :return: The angle in radians.
    """
    return atan2(v.v, v.u)

def angle_between(a: UV, b: UV) -> float:
    """
    Returns the angle between two vectors.
    :param a: The first vector.
    :param b: The second vector.
    :return: The angle in radians.
    """
    return atan2(cross(a, b), dot(a, b))


### UV constants ###
# Common UVs
ZERO = UV(0, 0)
LEFT = UV(-1, 0)
RIGHT = UV(1, 0)
UP = UV(0, -1)
DOWN = UV(0, 1)

# Shader math values
ONE = UV(1, 1)
CENTER = UV(0.5, 0.5)