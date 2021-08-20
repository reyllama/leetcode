"""
118. Pascal's Triangle

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        def pascal(arr):
            ans = []
            arr = [0] + arr + [0]
            for i in range(len(arr)-1):
                ans += [arr[i]+arr[i+1]]
            return ans
        
        base = [1]
        ans = [base]
        for _ in range(numRows-1):
            base = pascal(base)
            ans.append(base)

        return ans

"""
Runtime: 16 ms, faster than 74.77% of Python online submissions for Pascal's Triangle.
Memory Usage: 13.5 MB, less than 35.58% of Python online submissions for Pascal's Triangle.
"""