from rembg import remove
from PIL import Image


input = Image.open("lucy.jpg")

output = remove(input)

output.save("out.png")
