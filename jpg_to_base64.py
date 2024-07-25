import base64
import os

# Use relative paths based on the current working directory.
base_dir = os.getcwd()
images_dir = os.path.join(base_dir, 'images')
encoded_dir = os.path.join(base_dir, 'encoded_images')

# If the encoded_images directory does not exist, create it.
if not os.path.exists(encoded_dir):
    os.makedirs(encoded_dir)

while True:
    yol = input("Select a photo from the Images directory with the same name:")
    image_path = os.path.join(images_dir, f'{yol}.jpg')

    if not os.path.exists(image_path):
        print("Error: The selected file was not found in the Images directory. Please enter a valid file name.")
        continue

    output_path = os.path.join(encoded_dir, f'encoded_image_{yol}.txt')

    with open(image_path, 'rb') as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

    with open(output_path, 'w') as output_file:
        output_file.write(encoded_string)

    print(f"The Base64 code has been written to the {output_path} file")
    cikis = input("Press any key to continue, or press ‘e’ or ‘E’ to exit the program:")
    if cikis.lower() == 'e':
        break