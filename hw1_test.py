import data
import hw1
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
########################################################################################################################
    # Testing Vowel Count

    # Test for lowercase vowels
    def test_vowel_count1(self):
        function_input = "aeiou"
        expected = 5
        actual = hw1.vowel_count(function_input)
        self.assertEqual(actual, expected)
    # Test for uppercase vowels
    def test_vowel_count2(self):
        function_input = "AEIOU"
        expected = 5
        actual = hw1.vowel_count(function_input)
        self.assertEqual(actual, expected)

    # Test for uppercase and lowercase values in a string with spaces
    def test_vowel_count3(self):
        function_input = "Once Upon A Time In A Galaxy FAR FAR AWAY"
        expected = 15
        actual = hw1.vowel_count(function_input)
        self.assertEqual(actual, expected)


#  Part 2
#######################################################################################################################
    #Testing short_lists
    # test function for one short list
    def test_short_lists1(self):
        function_input = [[1,2,3],[4,5,6],[7,8,9],[],[1,2]]
        expected = [[1,2]]
        actual = hw1.short_lists(function_input)
        self.assertEqual(actual, expected)

    # test function for empty list
    def test_short_lists2(self):
        function_input = []
        expected = []
        actual = hw1.short_lists(function_input)
        self.assertEqual(actual, expected)

    # test with more than one "short list"
    def test_short_lists3(self):
        function_input = [[1,2], [1,1],[2]]
        expected = [[1,2], [1,1]]
        actual = hw1.short_lists(function_input)
        self.assertEqual(actual, expected)

########################################################################################################################
    # Part 3
    # Testing ascending_pairs

    def test_ascending_pairs1(self):
        function_input = [[1,2,3],[4,5,6],[7,8,9],[],[1,2]]
        expected = [[1,2,3],[4,5,6],[7,8,9],[],[1,2]]
        actual = hw1.ascending_pairs(function_input)
        self.assertEqual(actual, expected)
    # Test a few arbitrary lists
    def test_ascending_pairs2(self):
        function_input = [[2,1],[1,1],[2],[9009,1000],[10000, 5]]
        expected = [[1,2],[1,1],[2],[1000, 9009],[5, 10000]]
        actual = hw1.ascending_pairs(function_input)
        self.assertEqual(actual, expected)








        # Part 4


    # Part 5


    # Part 6


    # Part 7


    # Part 8





if __name__ == '__main__':
    unittest.main()
