# Author: Jorgé Sandoval
# Assignment 2
# Date: 10-04-2024

"""
This script performs the following actions:
1. Load an image from a specified file path in the local directory.
2. Change the image's color to grayscale.
3. Resize the image to a specific grid size (e.g., 300x300 pixels).
4. Save both the original and altered images.
"""

from PIL import Image

def load_image(file_path):
    return Image.open(file_path)

def convert_to_grayscale(image):
    return image.convert("L")

def resize_image(image, size=(300, 300)):
    return image.resize(size)

def save_image(image, path):
    image.save(path)

def main():
    # Step 1: Define the local image file path and the paths to save images
    image_file_path = "pat.jpeg"  # Replace with your local image file path
    original_image_path = "original_image.jpg"
    grayscale_image_path = "grayscale_image.jpg"
    resized_image_path = "resized_image.jpg"

    # Step 2: Load the image
    original_image = load_image(image_file_path)
    save_image(original_image, original_image_path)  # Save the original image
    
    # Step 3: Convert the image to grayscale
    grayscale_image = convert_to_grayscale(original_image)
    save_image(grayscale_image, grayscale_image_path)  # Save the grayscale image

    # Step 4: Resize the image
    resized_image = resize_image(grayscale_image)
    save_image(resized_image, resized_image_path)  # Save the resized image

if __name__ == "__main__":
    main()
