import unittest
import board_renamer as br
import image_name_matches as matches


class TestIntegration(unittest.TestCase):

    def test_integration(self):
        num_correct = 0
        num_total = 1  # len(matches.images_input)
        for i in range(num_total):
            key = matches.images_input[i]
            value = matches.images_output[i]
            new_filepath = br.main(key)
            if new_filepath == value:
                num_correct += 1
        percent_correct = num_correct/num_total
        self.assertEqual(percent_correct, 0.95)


if __name__ == '__main__':
    unittest.main()
