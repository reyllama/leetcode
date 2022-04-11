"""
1137. N-th Tribonacci Number

The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.
"""

class Solution:
    def tribonacci(self, n: int) -> int:
        # Bottom-up
        arr = [0,1,1] + [None]*(n-2)
        for i in range(3, n+1):
            arr[i]  =arr[i-1]+arr[i-2]+arr[i-3]
        return arr[n]

"""
class Solution:
    def tribonacci(self, n: int) -> int:
        # Bottom-up
        arr = [0,1,1] + [None]*(n-2)
        for i in range(3, n+1):
            arr[i]  =arr[i-1]+arr[i-2]+arr[i-3]
        return arr[n]
"""
