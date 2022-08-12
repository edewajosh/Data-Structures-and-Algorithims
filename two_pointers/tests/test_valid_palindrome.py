from unittest import TestCase

from valid_palindrome import Solution

class TestPalindrome(TestCase):

    def test_single_string(self):
        ans = Solution('Madam')
        self.assertEquals(ans.isPalindrome(), True)

    def test_word(self):
        ans = Solution('A man, a plan, a canal: Panama')
        self.assertEquals(ans.isPalindrome(), True)

    def test_non_palindrome(self):
        ans = Solution('palindrome')
        self.assertEquals(ans.isPalindrome(), False)
