from SCPSIG import *

# Generates a square gradient.

def sample_func(point: UV) -> Color:
    return color.vector(point.u, point.v, 0.5, 1)

generate_image(sample_func, "color_test")