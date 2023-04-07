from PIL import Image

# Define the image compressor function
def compress_image(image_path, quality=100):
    # Open the image file
    with Image.open(image_path) as img:
        # Compress the image using JPEG format and the specified quality
        img.save(image_path, optimize=True, quality=quality)

# Example usage
compress_image("input.jpg", quality=100)
