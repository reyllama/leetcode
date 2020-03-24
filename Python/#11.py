"""
11. Container With Most Water

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.


   +         +
   +         +   +
   + +       +   +
   + +   +   +   +
   + +   + + +   +
   + +   + + + + +
   + + + + + + + +
 + + + + + + + + +

The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water (blue section) the container can contain is 49.

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
"""

class Solution:
    def maxArea(self, height):
        if len(height)>1:
            length = len(height)-1
            maxx = (length*min(height[0], height[-1]))
            while length:
                points = {(height[i], height[i+length]) for i in range(len(height)-length)}
                maxx = max(maxx, length*max([min(i,v) for (i,v) in points]))
                length -= 1
            return maxx
        return None

""" Brute Force: Execution Time out"""

class Solution:
    def maxArea(self, height):
        i, j = 0, len(height)-1
        maxx = 0
        while j>i:
            area = (j-i)*min(height[i], height[j])
            maxx = max(maxx, area)
            if height[j]<height[i]:
                j-=1
            else:
                i+=1
        return maxx

"""
Runtime: 132 ms, faster than 62.26% of Python3 online submissions for Container With Most Water.
Memory Usage: 14.5 MB, less than 41.05% of Python3 online submissions for Container With Most Water.
"""
#             for i, cur in enumerate(height):
#



import time
arr = [i for i in range(1, 50000, 2)]
t0 = time.time()
x = Solution()
print(x.maxArea(arr))
print("{:.2f}s passed".format(time.time()-t0))
# import numpy as np
