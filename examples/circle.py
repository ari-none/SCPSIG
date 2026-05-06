from SCPSIG import *

# A simple circle.

def sample_func(point: UV) -> Color:
    point = point.centered()
    return color.WHITE if uv.length(point) <= 0.35 else color.BLACK

generate_image(sample_func, "circle")