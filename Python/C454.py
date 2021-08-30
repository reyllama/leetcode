"""
454. 4Sum II

Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:

0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
"""

class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        from collections import defaultdict
        
        A, B = defaultdict(int), defaultdict(int)
        a = []
        res = 0
        n = len(nums1)
        
        for i in range(n):
            for j in range(n):
                A[nums1[i]+nums2[j]] += 1
                B[nums3[i]+nums4[j]] += 1
                a.append(nums1[i]+nums2[j]) 
        
        for num in a:
            res += B[-num]
            
        return res

"""
Runtime: 1032 ms, faster than 24.17% of Python online submissions for 4Sum II.
Memory Usage: 14.8 MB, less than 9.92% of Python online submissions for 4Sum II.
"""