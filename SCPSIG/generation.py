from .color import Color
from .uv import UV
from collections.abc import Callable
import zlib
import struct
import os

def generate_image(func: Callable[[UV], Color], filename: str = "output", width: int = 512, height: int = 512) -> None:
    """
    Generates an image in the .png file format, according to a shader-like function.
    :param func: The function for generating the image, which takes a UV coordinate as an argument and returns a color.
    :param filename: The optional name for the output file.
    :param width: The optional image width.
    :param height: The optional image height.
    """
    pixels = [[None] * width for _ in range(height)]
    for x in range(width):
        for y in range(height):
            u = x / width
            v = y / height
            pixels[y][x] = func(UV(u, v))
    
    def make_png(width, height, pixels):
        signature = b'\x89PNG\r\n\x1a\n'
        ihdr_data = struct.pack('>IIBBBBB', width, height, 8, 6, 0, 0, 0)
        ihdr = make_chunk(b'IHDR', ihdr_data)
    
        raw_rows = []
        for y in range(height):
            row = b'\x00'
            for x in range(width):
                col = pixels[y][x]
                r, g, b, a = col.r, col.g, col.b, col.a
                row += struct.pack('BBBB', r, g, b, a)
            raw_rows.append(row)
    
        raw_data = b''.join(raw_rows)
        compressed = zlib.compress(raw_data)
        idat = make_chunk(b'IDAT', compressed)
    
        iend = make_chunk(b'IEND', b'')
    
        return signature + ihdr + idat + iend
    
    def make_chunk(chunk_type: bytes, data: bytes) -> bytes:
        chunk = chunk_type + data
        return struct.pack('>I', len(data)) + chunk + struct.pack('>I', zlib.crc32(chunk) & 0xFFFFFFFF)

    if not (os.path.exists("scpsig_output") and os.path.isdir("scpsig_output")):
        os.mkdir("scpsig_output")

    filename = f"scpsig_output/{filename}.png"
    
    png_bytes = make_png(width, height, pixels)
    with open(filename, 'wb') as f:
        f.write(png_bytes)