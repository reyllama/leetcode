"""
42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
"""
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        curMax = 0
        lmax, rmax = [], []
        for h in height:
            if h>curMax:
                lmax.append(h)
                curMax = h
            else:
                lmax.append(curMax)
        curMax = 0
        for h in height[::-1]:
            if h>curMax:
                rmax.append(h)
                curMax = h
            else:
                rmax.append(curMax)
        rmax = rmax[::-1]
        res = 0
        for i, h in enumerate(height):
            if i==0:
                continue
            elif i==len(height)-1:
                break
            res += max(0, min(lmax[i-1], rmax[i+1])-h) # ReLU
        return res

"""
Runtime: 64 ms, faster than 14.12% of Python online submissions for Trapping Rain Water.
Memory Usage: 15.2 MB, less than 6.54% of Python online submissions for Trapping Rain Water.
"""