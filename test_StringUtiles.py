import unittest 
from StringUtiles import IsPalindrome

class TestStringUtiles(unittest.TestCase):
    def test_palindrome(self):
        self.assertTrue(IsPalindrome("Racecar"))
        self.assertTrue(IsPalindrome("Hello"))
        self.assertTrue(IsPalindrome(""))
        self.assertTrue(IsPalindrome("A man a plan a canal Panama"))
    if __name__ == '__main__':
        unittest.main()