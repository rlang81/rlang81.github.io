from PIL import Image
import os

def generate_thumbnail(input_path, output_path, size=(600, 400)):
    """
    Generate thumbnail for an image.

    Args:
    - input_path: Path to the original image file.
    - output_path: Path to save the generated thumbnail.
    - size: Tuple (width, height) of the thumbnail size.
    """
    try:
        with Image.open(input_path) as img:
            img.thumbnail(size)
            img.save(output_path)
            print(f"Thumbnail generated: {output_path}")
    except Exception as e:
        print(f"Error generating thumbnail for {input_path}: {e}")

def generate_thumbnails(input_dir, output_dir):
    """
    Generate thumbnails for all images in the input directory and its subdirectories.

    Args:
    - input_dir: Path to the directory containing original images.
    - output_dir: Path to save the generated thumbnails.
    """
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                input_path = os.path.join(root, file)
                output_path = os.path.join(output_dir, os.path.relpath(input_path, input_dir))
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                generate_thumbnail(input_path, output_path)

if __name__ == "__main__":
    input_directory = "assets/img/photography"
    output_directory = "assets/img/thumbnails"

    generate_thumbnails(input_directory, output_directory)
