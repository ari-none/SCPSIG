from SCPSIG import *
from math import floor

# The "ErluM" pattern ; which doesn't mean anything. It's just for fun.

def sample_func(point: UV) -> Color:
    point = point.centered()
    grid_col: Color = color.MAGENTA if (floor(point.u * 10) + floor(point.v * 10)) % 2 == 0 else color.BLACK
    check = uv.distance(UV(0.25, 0.25), point) <= 0.15 or uv.distance(UV(-0.25, -0.25), point) <= 0.15
    return -grid_col if check else grid_col

generate_image(sample_func, "erlum")