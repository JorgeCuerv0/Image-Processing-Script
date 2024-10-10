# Image Processing Script

## Overview

This repository contains a Python script (`main.py`) that performs basic image processing tasks using the Python Imaging Library (PIL). The script can load an image, convert it to grayscale, resize it, and save both the original and processed images.

## Features

- **Load Image**: Load an image from a specified file path.
- **Convert to Grayscale**: Change the image's color to grayscale.
- **Resize Image**: Resize the image to a specific grid size (e.g., 300x300 pixels).
- **Save Images**: Save both the original and altered images to specified paths.

## Requirements

- Python 3.x
- Pillow (Python Imaging Library)

You can install the required library using pip:
```sh
pip install pillow
```

## Usage

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. **Place your image** in the repository directory and update the `image_file_path` variable in `main.py` with the image file name.

3. **Run the script**:
    ```sh
    python main.py
    ```

## Script Details

The script performs the following steps:

1. **Load the image**:
    ```python
    original_image = load_image(image_file_path)
    save_image(original_image, original_image_path)
    ```

2. **Convert the image to grayscale**:
    ```python
    grayscale_image = convert_to_grayscale(original_image)
    save_image(grayscale_image, grayscale_image_path)
    ```

3. **Resize the image**:
    ```python
    resized_image = resize_image(grayscale_image)
    save_image(resized_image, resized_image_path)
    ```

## Author

Jorgé Sandoval