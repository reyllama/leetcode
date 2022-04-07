"""
204. Count Primes

Given an integer n, return the number of prime numbers that are strictly less than n.
"""

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n <= 2:
            return 0
        
        arr = [1] * n
        arr[0] = arr[1] = 0
        
        for i in range(2, int(n**0.5)+1):
            if arr[i]:
                arr[i*i:i*(n//i+1):i] = [0] * len(arr[i*i:i*(n//i+1):i])
        return sum(arr)

"""
Runtime: 1365 ms, faster than 93.18% of Python online submissions for Count Primes.
Memory Usage: 91 MB, less than 88.38% of Python online submissions for Count Primes.
"""
