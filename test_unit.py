import unittest
import board_renamer as br
import numpy as np


class TestOnlyBlack(unittest.TestCase):

    def test_colors_to_white(self):
        color_arr = np.array([
            [
                [0, 255, 128],
                [64, 255, 128]
            ],
            [
                [128, 255, 128],
                [192, 255, 128]
            ]
        ])
        expect_arr = np.array([
            [
                [0, 255, 255],
                [64, 255, 255]
            ],
            [
                [128, 255, 255],
                [192, 255, 255]
            ]
        ])
        result_arr = br.only_black(color_arr)
        np.testing.assert_array_equal(result_arr, expect_arr)

    def test_grey_to_white(self):
        pass

    def test_black_to_black(self):
        pass


if __name__ == '__main__':
    unittest.main()
