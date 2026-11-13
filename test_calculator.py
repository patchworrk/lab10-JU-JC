import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(multiply(1,2), 2)
        self.assertEqual(multiply(100, 200), 20000)
        self.assertEqual(multiply(-9, -8), 72)
        self.assertEqual(multiply(-9, 8), -72)

    def test_divide(self): # 3 assertions
        self.assertEqual(divide(2, 4), 2)
        self.assertEqual(divide(2, 10), 5)
        self.assertEqual(divide(-2, 98), -49)
        self.assertEqual(divide(-2, -98), 49)

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            logarithm(0, 5)

    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(2,2), sqrt(8))
        self.assertEqual(hypotenuse(3, 4), sqrt(25))
        self.assertEqual(hypotenuse(3, -4), 5)
        self.assertNotEqual(hypotenuse(1, 1), 1)

    def test_sqrt(self): # 3 assertions
        self.assertEqual(sqrt(4), 2)
        self.assertEqual(sqrt(25), 5)
        self.assertNotEqual(sqrt(81), 81)

# Do not touch this
if __name__ == "__main__":
    unittest.main()