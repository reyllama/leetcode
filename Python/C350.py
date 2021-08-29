"""
350. Intersection of Two Arrays II

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

"""

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        A = Counter(nums1)
        ans = []
        
        for num in nums2:
            if A.get(num, 0) > 0:
                ans.append(num)
                A[num] -= 1
                
        return ans

"""
Runtime: 36 ms, faster than 62.54% of Python online submissions for Intersection of Two Arrays II.
Memory Usage: 13.7 MB, less than 14.00% of Python online submissions for Intersection of Two Arrays II.
"""