import unittest
from Assignment4 import fahrenheit_to_celsius, fibonacci

class TestAssignment4(unittest.TestCase):
    def test_fahrenheit_to_celsius(self):
        self.assertAlmostEqual(fahrenheit_to_celsius(212), 100)
        self.assertAlmostEqual(fahrenheit_to_celsius(32), 0)

        with self.assertRaises(ValueError):
            fahrenheit_to_celsius("Not a number")
    
    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(7), 13)

        with self.assertRaises(ValueError):
            fibonacci(-1)
        with self.assertRaises(ValueError):
            fibonacci("Not an integer")

if __name__ == '__main__':
    unittest.main()