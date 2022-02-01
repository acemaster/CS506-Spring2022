from PIL import Image
import os

def draw_firestation():
    img = Image.open(os.getcwd()+"/fire.jpeg")
    img.show()
    return

draw_firestation()

