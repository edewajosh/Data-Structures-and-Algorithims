class Solution:
    def isPalindrome(self, s: str) -> bool:
        val = s.lower()
        val = [i for i in val if not i.isdigit() and i.isalpha()]
        res = ''.join(val)
        if res[::-1] == res:
            return True
        else:
            return False

if __name__ == '__main__':
    sol = Solution()
    print(sol.isPalindrome('0P'))