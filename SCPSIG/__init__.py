__title__       = "Simple Crappy Pseudo-Shader Image Generation"
__description__ = "A pretty pointless image generation library made for very specific needs."
__version__     = "0.2.0"
__author__      = "Arinone"
__email__       = "no"
__license__     = "MIT"
__url__         = "https://github.com/you/SCPSIG"
__status__      = "Development"

__all__ = ["Color", "colors", "UV", "points", "generate_image"]

from .generation import generate_image
from .color import Color
from .uv import UV