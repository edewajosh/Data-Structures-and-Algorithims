"""
Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.

 

Example 1:
    Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]

Example 2:
    Input: nums = [1], k = 1
    Output: [1]
"""

def topKFrequent(nums, k):
    freq_map = {}
    for num in nums:
        if num not in freq_map:
            freq_map[num] = nums.count(num)
    sorted_freq_map = {k:v for k,v in sorted(freq_map.items(), key=lambda item: item[1], reverse=True)}
    return list(sorted_freq_map.keys())[:k]

if __name__ == '__main__':
    nums = [1,1,1,2,2,3] 
    k = 2
    print(topKFrequent(nums, k))
    