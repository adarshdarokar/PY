from tkinter import filedialog
from PIL import Image

file = filedialog.askopenfilename()

img = Image.open(file)

new_img = img.resize((800,600))

new_img.save("output.jpg")