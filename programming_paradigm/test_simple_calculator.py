import unittest
from simple_calculator import SimpleCalculator 

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator() #Initialize the calculator before each test

    def test_add(self):
        self.assertEqual(self.calc.add(3, 4), 7)
        self.assertEqual(self.calc.add(-1, -2), -3)
        self.assertEqual(self.calc.add(3, -1), 2)
        self.assertEqual(self.calc.add(-3, 1), -2)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(1, 2), -1)
        self.assertEqual(self.calc.subtract(2, 1), 1)
        self.assertEqual(self.calc.subtract(-2, 1), -3)
        self.assertEqual(self.calc.subtract(2, -4), 6)
        self.assertEqual(self.calc.subtract(2, 2), 0)
        self.assertEqual(self.calc.subtract(-3, -4), 1)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 2), 4)
        self.assertEqual(self.calc.multiply(2, 0), 0)
        self.assertEqual(self.calc.multiply(0, 2), 0)
        self.assertEqual(self.calc.multiply(1, 10), 10)
        self.assertEqual(self.calc.multiply(2, -3), -6)
        self.assertEqual(self.calc.multiply(-3, -4), 12)
        self.assertEqual(self.calc.multiply(2000000, 2000000), 4000000000000)

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 2), 3)
        self.assertEqual(self.calc.divide(2, 4), 0.5)
        self.assertEqual(self.calc.divide(-4, -2), 2)
        self.assertEqual(self.calc.divide(6, -3), -2)
        self.assertEqual(self.calc.divide(-6, 2), -3)

    def test_divide_by_zero(self):
        self.assertIsNone(self.calc.divide(3, 0))
        self.assertIsNone(self.calc.divide(-5, 0))
        self.assertIsNone(self.calc.divide(0, 0))
        

if __name__ == '__main__':
    unittest.main()