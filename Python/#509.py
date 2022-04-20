"""
509. Fibonacci Number

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.

Given n, calculate F(n).
"""

class Solution:
    def fib(self, n: int) -> int:
	# Bottom-up
        arr = [0, 1] + [None]*(n-1)
        for i in range(2, n+1):
            arr[i] = arr[i-1] + arr[i-2]
        return arr[n]

"""
Runtime: 37 ms, faster than 75.25% of Python3 online submissions for Fibonacci Number.
Memory Usage: 13.9 MB, less than 58.57% of Python3 online submissions for Fibonacci Number.
"""
