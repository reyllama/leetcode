"""
62. Unique Paths

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
"""

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        def fac(n):
            if n <= 1:
                return 1
            else:
                return n*fac(n-1)
        
        return fac(n+m-2) / fac(m-1) / fac(n-1)