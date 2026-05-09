"""Pre-defined color constants."""
from .color import Color

# Transparent pixel (alongside a transparency scale)
TRANSPARENT = Color(255, 255, 255, 0)

TRANSPARENT_100 = TRANSPARENT
TRANSPARENT_75 = Color(255, 255, 255, 63)
TRANSPARENT_50 = Color(255, 255, 255, 127)
TRANSPARENT_25 = Color(255, 255, 255, 191)

# Monochrome scales
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
GRAY = Color(127, 127, 127)

SHADE_0 = BLACK
SHADE_25 = Color(63, 63, 63)
SHADE_50 = GRAY
SHADE_75 = Color(191, 191, 191)
SHADE_100 = WHITE

# RGB & CMY primitives
RED = Color(255, 0, 0)
GREEN = Color(0, 255, 0)
BLUE = Color(0, 0, 255)

MAGENTA = Color(255, 0, 255)
CYAN = Color(0, 255, 255)
YELLOW = Color(255, 255, 0)

# Other known colors
PURPLE = Color(127, 0, 255)
PINK = Color(255, 192, 203)
HOT_PINK = Color(255, 0, 127)
ORANGE = Color(255, 127, 0)
BROWN = Color(127, 63, 0)
LIME = Color(127, 255, 0)
BLUER = Color(0, 127, 255)
PISS = Color(161, 201, 18)
SHIT = Color(56, 22, 5)

# Eeveelutions !
EEVEE_FUR = Color(186, 130, 61)
EEVEE_COLLAR = Color(244, 226, 185)
VAPOREON_SKIN = Color(126, 202, 226)
VAPOREON_SPINE = Color(43, 97, 119)
VAPOREON_FIN = Color(236, 233, 198)
JOLTEON_FUR = Color(254, 217, 107)
FLAREON_FUR = Color(235, 127, 66)
FLAREON_COLLAR = Color(230, 211, 152)