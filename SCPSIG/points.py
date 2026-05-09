"""Pre-defined UV point constants."""
from .uv import UV

# Common UV points
ZERO = UV(0, 0)
LEFT = UV(-1, 0)
RIGHT = UV(1, 0)
UP = UV(0, -1)
DOWN = UV(0, 1)

# Shader math values
ONE = UV(1, 1)
CENTER = UV(0.5, 0.5)

# unfunny garbage values
SIX_SEVEN = UV(6, 7)
TRUE_SIX_SEVEN = UV(67, 67)