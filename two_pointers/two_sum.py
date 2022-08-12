class Solution:

    """
    Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

    Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

    The tests are generated such that there is exactly one solution. You may not use the same element twice.

    Your solution must use only constant extra space.

    

    Example 1:

    Input: numbers = [2,7,11,15], target = 9
    Output: [1,2]
    Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
    Example 2:

    Input: numbers = [2,3,4], target = 6
    Output: [1,3]
    Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
    Example 3:

    Input: numbers = [-1,0], target = -1
    Output: [1,2]
    Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
    

    Constraints:

    2 <= numbers.length <= 3 * 104
    -1000 <= numbers[i] <= 1000
    numbers is sorted in non-decreasing order.
    -1000 <= target <= 1000
    The tests are generated such that there is exactly one solution.
    """

    def __init__(self, numbers, target):
        self.numbers = numbers
        self.target = target

    # def twoSum(self):
    #     for i in range(len(self.numbers)):
    #         for j in range(i+1,len(self.numbers)):
    #             add = self.numbers[i] + self.numbers[j]
    #             if add == self.target:
    #                 return [i+1, j+1]
                
    def two_sum(self):
        l, r = 0, len(self.numbers)-1
        while l < r:
            add = self.numbers[l] + self.numbers[r]

            if add < self.target:
                l += 1
            elif add > self.target:
                r -= 1
            else:
                return[l+1, r+1]


if __name__ == '__main__':
    sol = Solution([0,0,3,4], 0)
    sol_1 = Solution([2,7,11,15], 9)
    print(sol_1.two_sum())