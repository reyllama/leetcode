"""
  Longest Harmonious Subsequence

We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.
"""

class Solution:
    def findLHS(self, nums):
        from collections import defaultdict
        cache = defaultdict(int)
        for num in nums:
            cache[num] += 1
            cache[num-1] += 1
        while cache:
            t = max(cache.keys(), key=(lambda k: cache[k]))
            if t in nums and t+1 in nums:
                return max(cache.values())
            del cache[t]
        return 0


"""
Runtime: 544 ms
Memory Usage: 16.7 MB
"""

class Solution:
    def findLHS(self, A):
        count = collections.Counter(A)
        ans = 0
        for x in count:
            if x+1 in count:
                ans = max(ans, count[x] + count[x+1])
        return ans

"""
Runtime: 300 ms, faster than 78.66% of Python3 online submissions for Longest Harmonious Subsequence.
Memory Usage: 16 MB, less than 66.31% of Python3 online submissions for Longest Harmonious Subsequence.
"""
