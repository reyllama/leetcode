"""
88. Merge Sorted Array

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        c, i, j = 0, 0, 0
        
        while i<m+n and j<n:
            if i>=m+c:
                nums1[i] = nums2[j]
                i, j = i+1, j+1
                continue
            if nums1[i] >= nums2[j]:
                tmp = nums1[i:-1]
                nums1[i] = nums2[j]
                nums1[i+1:] = tmp
                c, i, j = c+1, i+1, j+1
            else:
                i += 1

"""
Runtime: 28 ms, faster than 41.23% of Python online submissions for Merge Sorted Array.
Memory Usage: 13.4 MB, less than 44.47% of Python online submissions for Merge Sorted Array.
"""