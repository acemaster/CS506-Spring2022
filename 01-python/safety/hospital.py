import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def draw_hospital():
    img = mpimg.imread('hospital-image.jpg')
    imgplot = plt.imshow(img)
    plt.show()

draw_hospital()
