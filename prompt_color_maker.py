import os
import numpy as np
from PIL import Image
import colorsys

# --- Configuration ---
IMAGE_SIZE = (2000, 2000)  # Full image size (background)
SQUARE_SIZE = (1000, 1000)  # Central square size
BACKGROUND = [(255, 255, 255),(0,0,0),(51,51,51),(102,102,102),(153,153,153),(204,204,204)]  # RGB background color (dark gray)

# HSV Sampling Parameters
HUE_STEP = 3  # Interval for Hue (0 to 360 degrees)
SAT_STEP = 0.1  # Interval for Saturation (0 to 1)
VAL_STEP = 0.1  # Interval for Value (0 to 1)

# Output Directory


def hsv_to_rgb(h, s, v):
    """Convert HSV (0-360, 0-1, 0-1) to RGB (0-255)."""
    r, g, b = colorsys.hsv_to_rgb(h / 360, s, v)
    return int(r * 255), int(g * 255), int(b * 255)

def create_colored_image(h, s, v, file_format="png", BG=(255, 255, 255)):
    """Generate an image with a fixed background and a colored square in the center."""
    img = Image.new("RGB", IMAGE_SIZE, BG)
    square_color = hsv_to_rgb(h, s, v)

    # Create the square
    square = Image.new("RGB", SQUARE_SIZE, square_color)
    
    # Paste it into the center of the image
    x_offset = (IMAGE_SIZE[0] - SQUARE_SIZE[0]) // 2
    y_offset = (IMAGE_SIZE[1] - SQUARE_SIZE[1]) // 2
    img.paste(square, (x_offset, y_offset))

    # Save image
    filename = f"{int(h):03}{int(s*100):03}{int(v*100):03}{int(BG[0]/256*100):02}.{file_format}"
    img.save(os.path.join(OUTPUT_DIR, filename), quality=95, optimize=True)

# --- Generate images ---
for b in BACKGROUND:
    for h in range(171, 360, HUE_STEP):
        for s in np.arange(0, 1.01, SAT_STEP):
            OUTPUT_DIR = f"HSV/{int(b[0]):03}/{int(h):03}/{int(s*100):03}/"
            os.makedirs(OUTPUT_DIR, exist_ok=True)
            for v in np.arange(0, 1.01, VAL_STEP):
                create_colored_image(h, s, v, file_format="png",BG=b)

print(f"Images saved in: {OUTPUT_DIR}")
