from SCPSIG import *
from math import sin

# A simple wave-like grid image.

col1 = Color(74, 214, 249)
col2 = Color(67, 224, 156)

def sample_func(point: UV) -> Color:
    g = abs(sin((point.u * 16) + (point.v * 16)))
    
    if 0.2 <= UV.distance(points.CENTER, point) <= 0.3:
        return Color(252, 251, 186)
    return Color.lerp(col1, col2, g)

generate_image(sample_func, "wave")