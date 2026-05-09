from SCPSIG import *

# A simple circle.

def sample_func(point: UV) -> Color:
    point = point.centered()
    return colors.WHITE if point.length() <= 0.35 else colors.BLACK

generate_image(sample_func, "circle")