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
        assert UV.length(self) != 0
        return self / UV.length(self)
    
    def centered(self) -> UV:
        """
        Returns a "centered" version of the UV (basically adds -0.5 to each coordinate). Especially useful for shader mathematics.
        :return: A centered version of the UV.
        """
        return UV(self.u - 0.5, self.v - 0.5)

    def length(self: UV) -> float:
        """
        Returns the length/magnitude of the vector.
        :param self: The vector.
        :return: The length/magnitude of the vector.
        """
        return sqrt(self.u**2 + self.v**2)

    def angle(self: UV) -> float:
        """
        Returns the UV vector's angle relative to the right. (positive U axis)
        :param self: The vector.
        :return: The angle in radians.
        """
        return atan2(self.v, self.u)

    ### Static methods for the class ###

    @staticmethod
    def dot(a: UV, b: UV) -> float:
        """
        Returns the dot product of two UV vectors.
        :param a: The first vector.
        :param b: The second vector.
        :return: The dot product.
        """
        return a.u * b.u + a.v * b.v

    @staticmethod
    def lerp(start: UV, end: UV, alpha: float) -> UV: # If called by a valid object rather than called as a static method, pass itself in the "start" value
        """
        Returns a UV value within the linear interpolation of two UVs.
        :param start: The initial UV.
        :param end: The target UV.
        :param alpha: The alpha interpolation value, between 0.0 and 1.0. (0.0 returns the initial UV, 1.0 returns the target UV)
        :return: The interpolated UV.
        """
        return UV(
            start.u * (1 - alpha) + end.u * alpha,
            start.v * (1 - alpha) + end.v * alpha
        )

    @staticmethod
    def cross(a: UV, b: UV) -> float:
        """
        Returns the cross product of two UV vectors.
        :param a: The first vector.
        :param b: The second vector.
        :return: The scalar of the cross product.
        """
        return a.u * b.v - a.v * b.u

    @staticmethod
    def distance(a: UV, b: UV) -> float:
        """
        Returns the distance between two UV points.
        :param a: The first point.
        :param b: The second point.
        :return: The distance between both points.
        """
        return UV.length(a - b)

    @staticmethod
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

    @staticmethod
    def angle_between(a: UV, b: UV) -> float:
        """
        Returns the angle between two vectors.
        :param a: The first vector.
        :param b: The second vector.
        :return: The angle in radians.
        """
        return atan2(UV.cross(a, b), UV.dot(a, b))