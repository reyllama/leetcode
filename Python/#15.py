"""
15. 3Sum

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

"""

class Solution:
    def threeSum(self, nums):
        arr = sorted(arr)
        ans = set()
        for i in range(len(arr)-2):
            if arr[i] > 0:
                break
            if i>0 and arr[i]==arr[i-1]:
                continue
            j, k = i+1, len(arr)-1
            while j<k:
                if arr[i] + arr[j] + arr[k] == 0:
                    ans.add((arr[i], arr[j], arr[k]))
                    j += 1
                    k -= 1
                elif arr[i] + arr[j] + arr[k] < 0:
                    j += 1
                else:
                    k -= 1
        return [list(item) for item in ans]

"""
Runtime: 1028 ms, faster than 50.18% of Python3 online submissions for 3Sum.
Memory Usage: 17.3 MB, less than 18.57% of Python3 online submissions for 3Sum.
"""
