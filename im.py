from PIL import Image
 
filePath = "data/images/a01-000u-s00-00.png"

img = Image.open(filePath)
width, height = img.size
print("The dimension of the image is", width, "x", height)