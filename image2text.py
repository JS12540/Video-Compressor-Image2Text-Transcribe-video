from PIL import Image

# Open an image file
image = Image.open("text.png")

# Cropping
cropped_image = image.crop((100, 100, 400, 400))  # (left, upper, right, lower)

# Rotating
rotated_image = image.rotate(45)  # Rotate by 45 degrees

# Other transformations
flipped_image = image.transpose(Image.FLIP_LEFT_RIGHT)  # Flip horizontally
grayscale_image = image.convert("L")  # Convert to grayscale

# Saving the transformed images
cropped_image.save("cropped_image.jpg")
rotated_image.save("rotated_image.jpg")
flipped_image.save("flipped_image.jpg")
grayscale_image.save("grayscale_image.jpg")
