
class Solution:
    """
    Description
    """
    def maxProfit(self, prices):
        largest = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                curr =  prices[j] - prices[i]
                if curr > largest:
                    largest = curr
        return largest


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProfit([7,6,4,3,1]))
