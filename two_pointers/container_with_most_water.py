class Solution:

    """
    You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

    Find two lines that together with the x-axis form a container, such that the container contains the most water.

    Return the maximum amount of water a container can store.

    Notice that you may not slant the container.

    

    Example 1:


    Input: height = [1,8,6,2,5,4,8,3,7]
    Output: 49
    Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
    Example 2:

    Input: height = [1,1]
    Output: 1
    

    Constraints:

    n == height.length
    2 <= n <= 105
    0 <= height[i] <= 104
    """

    def maxArea(self, height):
        l,r = 0, len(height)-1
        res = 0 
        
        while l < r:
            if height[l] < height[r]:
                res = max(res, min(height[l], height[r])*(r-l))
                l +=1
            elif height[r] <= height[l]:
                res = max(res, min(height[l], height[r])*(r-l))
                r -= 1
        return res

if __name__ == '__main__':
    sol = Solution()
    print(sol.maxArea([1,8,6,2,5,4,8,3,7]))