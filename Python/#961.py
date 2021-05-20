"""
961. N-Repeated Element in Size 2N Array

In a array nums of size 2 * n, there are n + 1 unique elements, and exactly one of these elements is repeated n times.

Return the element repeated n times.
"""

class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r = set()
        for item in nums:
            if item in r:
                return item
            else:
                r.add(item)

"""
Runtime: 164 ms, faster than 88.10% of Python online submissions for N-Repeated Element in Size 2N Array.
Memory Usage: 14.4 MB, less than 68.27% of Python online submissions for N-Repeated Element in Size 2N Array.
"""