from PIL import Image
import pytesseract as tesr
import numpy as np


CROP_HEIGHT_RATIO = 0.077  # Top text area of images is ~7.7% of height
VALUE_THRESHOLD = 30.0

def only_black(img_array):
    return_value = img_array
    hue, sat, val = np.split(return_value, 3, axis=2)
    val = np.where(val<VALUE_THRESHOLD, 0, 255)
    return_value = np.concatenate((hue, sat, val), axis=2)
    return return_value


def main(input_file):
    return_value = ""
    # Get image from image file
    try:
        board_image = Image.open(input_file)
        # Find crop height (7.7% of height) & crop
        crop_height = round(board_image.height*CROP_HEIGHT_RATIO)
        top_region_box = (0, 0, board_image.width, crop_height)
        top_region = board_image.crop(top_region_box)
        top_region = top_region.convert("HSV")
        # TODO: Process image
        top_region_arr = np.asarray(top_region)
        top_region_arr = only_black(top_region_arr)
        #top_region = top_region.convert("1")
        #new_size = (top_region.width*2, top_region.height*2)
        #top_region = top_region.resize(new_size)
        # Recognize text
        return_value = tesr.image_to_string(top_region)
    except IOError:
        return_value = None
    # TODO: Check if text matches expected format
    # TODO: If close match, edit close text to work
    # Return text or None (if no match)
    print(return_value)
    return return_value


def wrapper():
    pass


if __name__ == '__main__':
    wrapper()
