from SCPSIG import *
from math import floor

# The "ErluM" pattern ; which doesn't mean anything. It's just for fun.

def sample_func(point: UV) -> Color:
    point = point.centered()
    grid_col = colors.MAGENTA if (floor(point.u * 10) + floor(point.v * 10)) % 2 == 0 else colors.BLACK
    check = UV.distance(point, UV(0.25, 0.25)) <= 0.15 or UV.distance(point, UV(-0.25, -0.25)) <= 0.15
    return -grid_col if check else grid_col # Color inversion is directly done by putting a minus symbol in front of a color!

generate_image(sample_func, "erlum")