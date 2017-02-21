import numpy as np
from matplotlib import pyplot as plt
import cv2

def load_img(src):
    return cv2.imread(src, 1)

def simple_get_skin(img):
    B, G, R = cv2.split(img)
    skin = np.zeros(img.shape, dtype=np.uint8)
    mask = (
        (B > 20) &
        (R > 95) &
        (G > 40) &
        # (abs(R-G)) > 15 &  # this line get really bad results
        (R > B) &
        (R > G)
   )
    skin[mask] = 255
    return skin

def hist_get_skin(img):
    skin = np.zeros(img.shape, dtype=np.uint8)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
    show(hist)
    return skin

def show(img):
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def plot_mask(mask):
    img = np.zeros(mask.shape, dtype=np.uint8)
    img[mask] = 255
    show(img)

if __name__ == "__main__":
    src = 'data/Pratheepan_Dataset/FacePhoto/0520962400.jpg'
    src = 'data/Pratheepan_Dataset/FacePhoto/mandy-moore-face-wallpapers_1913_1600.jpg'
    img = load_img(src)
    #skin = simple_get_skin(img)
    skin = hist_get_skin(img)
    show(skin)

