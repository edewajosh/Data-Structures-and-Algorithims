from unittest import TestCase

from two_sum import Solution

class TestTwoSum(TestCase):

    def test_adjucent_numbers(self):
        sol = Solution([2,7,11,15], 9)
        self.assertEquals(sol.two_sum(), [1,2])