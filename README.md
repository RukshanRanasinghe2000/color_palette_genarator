# color_palette_genarator V1.0.0.
 color palette generator using images. based on python and FastAPI 

 # 🖌️ RGB to HEX Color Extraction

This project provides a Python utility for extracting dominant colors from an image using K-Means clustering.  
It converts RGB values into HEX format and returns a structured output of the most prominent colors.

# 📜 Features
- Convert RGB color values to HEX format.
- Extract dominant colors from an image using K-Means clustering.
- Handle both RGB and RGBA images.
- Return extracted colors as RGB and HEX representations.
  
# Example Output

```json
{
    "Color 1": {
        "RGB": [0.85, 0.32, 0.12],
        "Hex": "#d7521e"
    },
    "Color 2": {
        "RGB": [0.10, 0.65, 0.24],
        "Hex": "#1aad3d"
    },
    "Color 3": {
        "RGB": [0.92, 0.85, 0.13],
        "Hex": "#ebd822"
    }
}
```
# ⚙️ Configuration
- n_colors (int): Number of dominant colors to extract (default is 3).
- image (ndarray): Image loaded using skimage.io.imread() or similar methods.

# ✅ Requirements
Ensure you have the following packages installed:

- Python 3.10+
- NumPy
- scikit-image
- scikit-learn

# 🚀 About UI
The UI is simple and developed with HTMX and Tailwind.
