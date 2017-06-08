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
            [[1], [1]],
            [[1], [1]]
        ])
        result_arr = br.only_black(color_arr)
        np.testing.assert_array_equal(result_arr, expect_arr)

    def test_grey_to_white(self):
        grey_arr = np.array([
            [
                [0, 0, 50],
                [64, 0, 100]
            ],
            [
                [128, 0, 150],
                [192, 0, 200]
            ]
        ])
        expect_arr = np.array([
            [[1], [1]],
            [[1], [1]]
        ])
        result_arr = br.only_black(grey_arr)
        np.testing.assert_array_equal(result_arr, expect_arr)

    def test_blackish_to_black(self):
        black_arr = np.array([
            [
                [0, 0, 0],
                [64, 0, 10]
            ],
            [
                [128, 0, 20],
                [192, 0, 30]
            ]
        ])
        expect_arr = np.array([
            [[0], [0]],
            [[0], [0]]
        ])
        result_arr = br.only_black(black_arr)
        np.testing.assert_array_equal(result_arr, expect_arr)


if __name__ == '__main__':
    unittest.main()
