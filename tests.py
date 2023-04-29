from PIL import Image

# Open the two images
img_box = Image.open("box.png")
img_box1 = Image.open("box1.png")

# Copy the content of img_box to img_box1
img_box1.paste(img_box, (0, 0))

# Save the modified image
img_box1.save("box1.png")