"""
Given an integer array nums, return an array answer such that answer[i] is 
equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""
import math

def productExceptSelf(nums):
    ans = []
    index = 0
    current = nums[0]
    for i in range(1, len(nums)+1):
        # data = []
        # for j in range(len(nums)):
        #     if j == i:
        #         continue
        #     data.append(nums[j])
        # ans.append(math.prod(data))
        
        # remove the second loop
        current = nums.pop(index)
        ans.append(math.prod(nums))
        nums.insert(index, current)
        index = i
    return ans

if __name__ == '__main__':
    nums = [-1,1,0,-3,3]
    print(productExceptSelf(nums))
    