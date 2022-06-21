"""
Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the 
letters of a different word or phrase, typically using all 
the original letters exactly once.

 

Example 1:

    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:

    Input: strs = [""]
    Output: [[""]]

Example 3:

    Input: strs = ["a"]
    Output: [["a"]]
"""

def groupAnagrams(strs):
    ans = []
    ana_map = {}
    
    for st in strs:
        work = ''.join(sorted(st))
        if work in ana_map:
            ana_map[work].append(st)
        else:
            ana_map[work] = [st]

    for v in ana_map.values():
        ans.append(v)
    return ans
if __name__ == '__main__':
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(groupAnagrams(strs))
    