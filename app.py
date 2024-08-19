import os
import time
from PIL import Image, ImageDraw, ImageFont

# Display watermarking options
print("1. Text only")
print("2. Logo only")
print("3. Both text and logo")
choice = int(input("Choose an option (1, 2, or 3): "))

# Set up directories
image_dir = "images/"
logo_dir = "logo/"
output_dir = "water_marked_images"
valid_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff")

# Create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Get list of image files
image_files = os.listdir(image_dir)

# Handle logo-related options
if choice == 2 or choice == 3:
    transparency = int(input("Enter logo transparency level (0 = fully transparent, 150 = opaque): "))
    logo_files = [f for f in os.listdir(logo_dir) if f.lower().endswith(valid_extensions) and not f.startswith('.')]
    if not logo_files:
        raise FileNotFoundError("No valid logo file found in the /logo directory.")
    logo_path = os.path.join(logo_dir, logo_files[0])
    logo = Image.open(logo_path)
    logo_size = logo.size

# Handle text-related options
if choice == 1 or choice == 3:
    watermark_text = input("Enter watermark text: ")
    text_size = int(input("Enter text size (default = 72): "))
    transparency = int(input("Enter text transparency level (0 = fully transparent, 100 = opaque): "))

# Process each image in the directory
for file in image_files:
    if not file.lower().endswith(valid_extensions):
        continue
    
    image_path = os.path.join(image_dir, file)
    image = Image.open(image_path)

    if choice == 1:  # Text watermark
        transparent_layer = Image.new("RGBA", image.size)
        draw = ImageDraw.Draw(transparent_layer, "RGBA")
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", text_size)

        # Calculate text size and position
        bbox = draw.textbbox((0, 0), watermark_text, font=font)
        text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
        text_position = ((image.size[0] - text_width) / 2, (image.size[1] - text_height) / 2)

        # Draw watermark text
        draw.text(text_position, watermark_text, font=font, fill=(255, 255, 255))
        mask = transparent_layer.convert("L").point(lambda x: min(x, transparency))
        transparent_layer.putalpha(mask)
        image.paste(transparent_layer, None, transparent_layer)
        print("Text watermark applied.")
    
    elif choice == 2:  # Logo watermark
        masklogo = logo.convert("L").point(lambda x: min(x, transparency))
        logo_position = (int(image.size[0] / 2 - logo_size[0] / 2), int(image.size[1] / 2 - logo_size[1] / 2))
        image.paste(logo, logo_position, masklogo)
        print("Logo watermark applied.")
    
    elif choice == 3:  # Both text and logo watermark
        masklogo = logo.convert("L").point(lambda x: min(x, transparency))
        logo_position = (int(image.size[0] / 2 - logo_size[0] / 2), int(image.size[1] / 2 - logo_size[1] / 2))
        image.paste(logo, logo_position, masklogo)

        transparent_layer = Image.new("RGBA", image.size)
        draw = ImageDraw.Draw(transparent_layer, "RGBA")
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", text_size)

        # Calculate text size and position
        bbox = draw.textbbox((0, 0), watermark_text, font=font)
        text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
        text_position = ((image.size[0] - text_width) / 2, (image.size[1] + logo_size[1]) / 2)

        # Draw watermark text
        draw.text(text_position, watermark_text, font=font, fill=(255, 255, 255))
        mask = transparent_layer.convert("L").point(lambda x: min(x, transparency))
        transparent_layer.putalpha(mask)
        image.paste(transparent_layer, None, transparent_layer)
        print("Text and logo watermark applied.")

    # Save the watermarked image
    image.save(os.path.join(output_dir, "WM_" + file))

print("Saving images...")
time.sleep(2)
print("Finished.")
