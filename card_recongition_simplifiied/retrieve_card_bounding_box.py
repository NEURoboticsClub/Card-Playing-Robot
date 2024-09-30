import cv2
import numpy as np
from scipy.ndimage import center_of_mass


def get_bounding_box_of_one_card(img) -> (int, int, int, int):
    '''
    Get bounding box of a given card

    Arguments:
    img: RGB Color array as numpy array

    Returns:
    (min_x, min_y, max_x, max_y)
    '''
    grey_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    threshold_value = 200 
    _, mask = cv2.threshold(grey_img, threshold_value, 255, cv2.THRESH_BINARY)

    masked_img = np.zeros_like(img)
    masked_img[mask == 255] = img[mask == 255]
    masked_img[masked_img != 255] = 0

    masked_img = cv2.cvtColor(masked_img, cv2.COLOR_RGB2GRAY)

    ys, xs = np.where(masked_img / 255 == 1)

    min_x, max_x = xs.min(), xs.max()
    min_y, max_y = ys.min(), ys.max()

    return (min_x, min_y, max_x, max_y)
    