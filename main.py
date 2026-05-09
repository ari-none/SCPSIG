from SCPSIG import *
from math import ceil, sin

# The beautifully ugly logo for SCPSIG !

def sample_func(point: UV) -> Color:
    point = point.centered()
    if point.length() <= 0.1:
        return colors.EEVEE_COLLAR
    if point.length() <= 0.375:
        if abs(ceil((point.u + point.v*1.8) * 10.5)) > 3:
            g = UV.distance(points.CENTER, point) - 0.15
            return colors.EEVEE_FUR * Color.vector(g, g, g, 1)
        else:
            return colors.EEVEE_FUR * Color.vector(abs(sin(point.u * point.v)), 1, 1, 1)
    else:
        return Color(128, 0, 64) * Color.vector(sin((point.u + 0.001) / (0.01 + point.v * 0.15)), 1, 1, 1)

generate_image(sample_func)