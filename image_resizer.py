import os
from PIL import Image

def resize_images(input_folder, output_folder, width, height, output_format=None):
    """
    Resize all images in a folder and save them to another folder.
    
    Args:
        input_folder (str): Path to the folder containing input images.
        output_folder (str): Path to save resized images.
        width (int): Desired width in pixels.
        height (int): Desired height in pixels.
        output_format (str, optional): Format to save images in ('JPEG', 'PNG', etc.). If None, keeps original format.
    """
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)

        # Skip if it's not a file
        if not os.path.isfile(file_path):
            continue

        try:
            with Image.open(file_path) as img:
                # Resize image
                resized_img = img.resize((width, height), Image.LANCZOS)

                # Keep original format if not specified
                save_format = output_format if output_format else img.format

                # Build output file path
                base_name = os.path.splitext(filename)[0]
                ext = save_format.lower() if output_format else img.format.lower()
                output_file_path = os.path.join(output_folder, f"{base_name}.{ext}")

                # Save resized image
                resized_img.save(output_file_path, save_format)
                print(f"[OK] Resized and saved: {output_file_path}")

        except Exception as e:
            print(f"[ERROR] Could not process {filename}: {e}")

if __name__ == "__main__":
    # Example usage
    input_dir = "input_images"       # Folder with your images
    output_dir = "resized_images"    # Where to save resized images
    target_width = 800               # New width in pixels
    target_height = 600              # New height in pixels
    format_conversion = None         # Change to 'JPEG' or 'PNG' if needed

    resize_images(input_dir, output_dir, target_width, target_height, format_conversion)
