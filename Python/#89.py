"""
89. Gray Code

An n-bit gray code sequence is a sequence of 2n integers where:

    Every integer is in the inclusive range [0, 2n - 1],
    The first integer is 0,
    An integer appears no more than once in the sequence,
    The binary representation of every pair of adjacent integers differs by exactly one bit, and
    The binary representation of the first and last integers differs by exactly one bit.

Given an integer n, return any valid n-bit gray code sequence.
"""

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        bits = [None] * (2**n)
        memo = dict()
        bits[0] = "0"*n
        bits[-1] = "1"+"0"*(n-1)
        memo[bits[0]] = True
        memo[bits[-1]] = True
        for i in range(1, len(bits)-1):
            for pos in range(n):
                new = str(1-int(bits[i-1][pos]))
                new_bit = bits[i-1][:pos] + new + bits[i-1][pos+1:] if pos < n-1 else bits[i-1][:pos] + new
                if not memo.get(new_bit, False):
                    memo[new_bit] = True
                    bits[i] = new_bit
                    break
        for i in range(len(bits)):
            bits[i] = int(bits[i], 2)
        return bits

"""
Runtime: 320 ms, faster than 12.03% of Python online submissions for Gray Code.
Memory Usage: 24.4 MB, less than 6.02% of Python online submissions for Gray Code.
"""
