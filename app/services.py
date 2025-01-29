import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from skimage.util import img_as_float
from skimage.io import imread


def rgb_to_hex(rgb):
    """
        Convert an RGB color value (range 0-1) to a HEX string.
        Parameters:
        rgb (array-like): RGB values where each component is between 0 and 1.

        Returns:
        str: HEX color code.
    """
    return "#{:02x}{:02x}{:02x}".format(
        int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255)
    )



def process_image(image_path, n_colors=3):
    """
       Process an image to extract dominant colors using K-Means clustering.
       Parameters:
       image_path (str): Path to the image file.
       n_colors (int): Number of dominant colors to extract (default is 3).

       Returns:
       tuple:
           - centers (ndarray): Array of RGB values of extracted colors.
           - hex_colors (list): List of HEX color codes corresponding to extracted colors.
       """

    # Load and prepare the image
    logo = img_as_float(imread("test/test.jpg"))  # Fixed: Add `image_path` parameter
    print(f"Image shape: {logo.shape}")

    # Handle RGBA to RGB conversion if necessary
    if logo.shape[-1] == 4:  # If alpha channel exists
        print("Converting RGBA to RGB...")
        rgb_logo = np.ones((logo.shape[0], logo.shape[1], 3))
        alpha = logo[:, :, 3]
        for i in range(3):
            rgb_logo[:, :, i] = logo[:, :, i] * alpha + (1 - alpha)
        logo = rgb_logo  # Use converted RGB logo
    else:
        rgb_logo = logo

    print(f"RGB Image shape: {rgb_logo.shape}")

    # Reshape the image for clustering
    h, w = rgb_logo.shape[:2]
    image_array = rgb_logo.reshape((h * w, 3))

    # Perform k-means clustering
    kmeans = KMeans(n_clusters=n_colors, random_state=42, n_init=10)
    kmeans.fit(image_array)

    # Get labels and cluster centers (get RGB values)
    labels = kmeans.labels_
    centers = kmeans.cluster_centers_

    hex_colors = [rgb_to_hex(color) for color in centers]

    return centers, hex_colors
