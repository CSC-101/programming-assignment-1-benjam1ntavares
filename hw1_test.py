import hw1
import unittest
import data


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


# Part 3
########################################################################################################################
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
#######################################################################################################################
    #testing add prices

    # test not exceeding 99 cents
    def test_add_prices1(self):
        function_input = data.Price(26,25), data.Price(10,10)
        expected = data.Price(36,35)
        actual = hw1.add_prices(function_input[0], function_input[1])
        self.assertEqual(actual,expected)


    # test exceeding 99 cents
    def test_add_prices2(self):
        function_input = data.Price(26,99), data.Price(10,10)
        expected = data.Price(37,9)
        actual = hw1.add_prices(function_input[0], function_input[1])
        self.assertEqual(actual,expected)

    #test if adding purely cents will work to increase the dollar count even if the amount of cents already exceeds 99
    def test_add_prices3(self):
        function_input = data.Price(0,100), data.Price(0,200)
        expected = data.Price(3,0)
        actual = hw1.add_prices(function_input[0], function_input[1])
        self.assertEqual(actual,expected)


# part 5
#######################################################################################################################
    # testing rectangle_area

    # basic arbitrary test
    def test_rectangle_area1(self):
        function_input = data.Rectangle(data.Point(1,2), data.Point(3,4))
        expected = 4
        actual = hw1.rectangle_area(function_input)
        self.assertEqual(actual,expected)


    # test what happens if the rectangle begins in the negative axis
    def test_rectangle_area2(self):
        function_input = data.Rectangle(data.Point(-2,2), data.Point(2,-2))
        expected = 16
        actual = hw1.rectangle_area(function_input)
        self.assertEqual(actual,expected)

    # test fully in the negative quadrant
    def test_rectangle_area3(self):
        function_input = data.Rectangle(data.Point(-2,-4), data.Point(0,-6))
        expected = 4
        actual = hw1.rectangle_area(function_input)
        self.assertEqual(actual,expected)

    # test if there is no area
    def test_rectangle_area4(self):
        function_input = data.Rectangle(data.Point(-2,-4), data.Point(0,-4))
        expected = 0
        actual = hw1.rectangle_area(function_input)
        self.assertEqual(actual,expected)


# Part 6
#######################################################################################################################
    # testing books_by_author

    def test_books_by_author(self):
        function_input1 = 'george' # author
        function_input2 = [data.Book(['james', 'george'], 'the dragon'),data.Book(['james','john'],
                          'the dragon2'), data.Book(['james'], 'the dragon3') ,
                           data.Book(['george', 'james'], 'the gerbel')]


        result = hw1.books_by_author(function_input1, function_input2)
        expected = [data.Book(['james','george'], 'the dragon'), data.Book(['george','james'], 'the gerbel')]
        self.assertEqual(expected, result)

    def test_books_by_author2(self):
        function_input1 = 'george'
        function_input2 = [data.Book(['james', 'george'], 'the dragon'),data.Book(['james','john'],'quest')]
        result = hw1.books_by_author(function_input1,function_input2)
        expected = [data.Book(['james', 'george'], 'the dragon')]
        self.assertEqual(expected,result)



# Part 7
#######################################################################################################################
    # Test inner circle
    # test to create a circle about the origin
    def test_circle_bound1(self):
        function_input = data.Rectangle(data.Point(-1,1), data.Point(1, -1))
        expected = data.Circle(data.Point(0, 0), 1)
        actual = hw1.circle_bound(function_input)
        self.assertEqual(actual, expected)

    # test to make a circle in the negative quadrant
    def test_circle_bound2(self):
        function_input = data.Rectangle(data.Point(-4,0), data.Point(0, -4))
        expected = data.Circle(data.Point(-2, -2), 2)
        actual = hw1.circle_bound(function_input)
        self.assertEqual(actual,expected)

    def test_circle_bound3(self):
        function_input = data.Rectangle(data.Point(-4,-4), data.Point(0, -8))
        expected = data.Circle(data.Point(-2, -6), 2)
        actual = hw1.circle_bound(function_input)
        self.assertEqual(actual,expected)

# Part 8
#######################################################################################################################
    # test below_pay average with arbitrary payrates
    def test_below_pay_average1(self):
        function_input = [data.Employee('john', 100), data.Employee('james', 100),
                          data.Employee('will', 100), data.Employee('bob', 100),
                          data.Employee('george', 44), data.Employee('joey', 32)]
        expected = ['george', 'joey']
        actual = hw1.below_pay_average(function_input)
        self.assertEqual(actual,expected)

    # test with more arbitrary numbers
    def test_below_pay_average2(self):
        function_input = [data.Employee('john', 0), data.Employee('james', 0),
                          data.Employee('will', 0), data.Employee('bob', 0),
                          data.Employee('george', 4), data.Employee('joey', 32)]
        expected = ['john', 'james','will','bob','george']
        actual = hw1.below_pay_average(function_input)
        self.assertEqual(actual,expected)


if __name__ == '__main__':
    unittest.main()
