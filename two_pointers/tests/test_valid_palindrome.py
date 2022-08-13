from unittest import TestCase

from valid_palindrome import Solution

class TestPalindrome(TestCase):

    def test_single_string(self):
        ans = Solution('Madam')
        self.assertEqual(ans.isPalindrome(), True)

    def test_word(self):
        ans = Solution('A man, a plan, a canal: Panama')
        self.assertEqual(ans.isPalindrome(), True)

    def test_non_palindrome(self):
        ans = Solution('palindrome')
        self.assertEqual(ans.isPalindrome(), False)
