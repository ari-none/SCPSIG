from SCPSIG import *
from math import ceil, sin

# The beautifully ugly logo for SCPSIG !

def sample_func(point: UV) -> Color:
    point = point.centered()
    if uv.length(point) <= 0.1:
        return color.WHITE
    if uv.length(point) <= 0.35:
        if abs(ceil((point.u + point.v*0.8) * 9.5)) > 3:
            g = uv.distance(uv.CENTER, point) - 0.15
            return color.CYAN * color.vector(g, g, g, 1)
        else:
            return color.YELLOW * color.vector(abs(sin(point.u * point.v)), 1, 1, 1)
    else:
        return Color(128, 0, 64) * color.vector(sin((point.u + 0.001) / (0.01 + point.v * 0.15)), 1, 1, 1)

generate_image(sample_func)