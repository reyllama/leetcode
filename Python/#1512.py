"""
1512. Number of Good Pairs

Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.



Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.

Example 3:

Input: nums = [1,2,3]
Output: 0


Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100

"""

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        t = [nums.count(x) for x in set(nums)]
        return int(sum([n*(n-1)/2 for n in t if n>1]))

"""
Runtime: 36 ms, faster than 66.67% of Python3 online submissions for Number of Good Pairs.
Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Number of Good Pairs.
"""

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        t = [nums.count(x) for x in set(nums) if nums.count(x) > 1]
        return int(sum([n*(n-1)/2 for n in t]))

"""
Runtime: 44 ms, faster than 66.67% of Python3 online submissions for Number of Good Pairs.
Memory Usage: 13.7 MB, less than 100.00% of Python3 online submissions for Number of Good Pairs.
"""
