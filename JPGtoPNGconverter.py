import sys
import os
from PIL import Image

# Grab first and second arguments from command line
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# Check if the output folder exists; if not, create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through the files in the image folder
for filename in os.listdir(image_folder):
    # Combine folder path and filename correctly
    file_path = os.path.join(image_folder, filename)
  
    
    try:
        # Open the image only if it's a valid file
        img = Image.open(file_path)

        # Remove file extension and get clean name
        clean_name = os.path.splitext(filename)[0]  # [0] gives just the name, excluding the extension

        print(clean_name)

        # (Optional) Save processed images in the output folder
        # e.g., Save as PNG
        img.save(os.path.join(output_folder, f"{clean_name}.png"))

    except Exception as e:
        print(f"Skipping file {filename} due to an error: {e}")