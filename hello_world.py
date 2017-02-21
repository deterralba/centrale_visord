import numpy as np
from matplotlib import pyplot as plt
import cv2

def load_image(src, COLOR=True):
    img = cv2.imread(src, 1)
    print('{}x{} pixels'.format(*img.shape))

    if not COLOR:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def count_pxl(src, k, BGR=False):
    img = cv2.imread(src, 1)
    if not BGR:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #x = np.where(img[0] == k[0])# and img[1] == k[1] and img[2] == k[2])
    x = np.where((img[:,:,0] == k[0] and img[:,:,1] == k[1]).all())# and img[2] == k[2])
    print(x)
    return len(x)
    # return np.sum(img == k) shorter version

if __name__ == '__main__':
    src = 'sf.jpg'
    # load_image(src)
    #print(count_pxl(src, 124))
    print(count_pxl(src, [124, 53, 32], BGR=True))
