from PIL import Image

# Open the image file
image_path = 'DBBT\piece1.png'  # Replace with the path to your image file
image = Image.open(image_path)

# Display some information about the image

def get_image_format():

    print('Image format:', image.format)
    return image.format

def get_image_size():

    print('Image format:', image.size)
    return image.size

def get_image_mode():

    print('Image format:', image.mode)
    return image.mode


# Optionally, you can show the image using an external viewer
# image.show()