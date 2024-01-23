from PIL import Image
import os

def resize_images(input_folder, output_folder, new_size=(300, 300)):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of all files in the input folder
    files = os.listdir(input_folder)

    for file_name in files:
        input_path = os.path.join(input_folder, file_name)
        output_path = os.path.join(output_folder, file_name)

        # Open and resize the image
        with Image.open(input_path) as img:
            img_resized = img.resize(new_size, Image.ANTIALIAS)

            # Save the resized image to the output folder
            img_resized.save(output_path)

if __name__ == "__main__":
    # Replace these paths with your actual input and output folder paths
    input_folder_path = "path/to/input/folder"
    output_folder_path = "path/to/output/folder"

    # Resize images in the input folder and save them to the output folder
    resize_images(input_folder_path, output_folder_path)
