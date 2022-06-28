def lengthOfLongestSubstring(s):
    longest = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if s[j] in s[:j]:
                break;
            else:
                if len(s[:j+1]) > longest:
                    longest = len(s[:j+1])
    return longest

if __name__ == '__main__':
    s = "abcabcbb"
    s1 = "bbbbb"
    s2 = "pwwkew"
    print(lengthOfLongestSubstring(s))
    print(lengthOfLongestSubstring(s1))
    print(lengthOfLongestSubstring(s2))