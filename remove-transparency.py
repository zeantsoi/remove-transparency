import os
from PIL import Image

# Absolute path to this script
scriptdir = os.path.dirname(os.path.abspath(__file__))

# Walk through directory
for root, subfolders, files in os.walk(scriptdir):
    for file in files:
        try:
            image = Image.open(os.path.join(scriptdir, root, file))
            # If image has an alpha channel
            if image.mode == 'RGBA':
                # Create a blank background image
                bg = Image.new('RGB', image.size, (255, 255, 255))
                # Paste image to background image
                bg.paste(image, (0, 0), image)
                # Save pasted image as image
                bg.save(os.path.join(scriptdir, root, file), "PNG")

        except:
            pass