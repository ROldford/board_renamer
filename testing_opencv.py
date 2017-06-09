import numpy as np
import cv2


def main():
    img = cv2.imread('testing/Board00001.jpeg')
    cv2.startWindowThread()
    cv2.namedWindow('test')
    cv2.imshow('test', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()