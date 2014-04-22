# Remove PNG Transparency

(Or, more accurately, replace it with a solid fill color)

This is a Python script that recursively crawls through the directories located in the same directory as the script. It checks each image file for alpha transparency – when an alpha transparent image is found, the image is overlaid on top a solid white background and re-saved.

Perfect for use cases where transparency needs to be replaced wholesale as a batch.

### Usage
Place this script in the directory you want to crawl, then run it:

    python remove-transparency.py

### Dependencies
[PIL](http://www.pythonware.com/products/pil/)
