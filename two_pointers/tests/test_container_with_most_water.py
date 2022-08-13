import imp
from unittest import TestCase

from container_with_most_water import Solution

class TestContainerWithMostWater(TestCase):

    def test_more_than_two(self):
        sol = Solution()
        self.assertEqual(sol.maxArea([1,8,6,2,5,4,8,3,7]), 49)
        self.assertEqual(sol.maxArea([1,1]), 1)