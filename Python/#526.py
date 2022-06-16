"""
526. Beautiful Arrangement

Suppose you have n integers labeled 1 through n. A permutation of those n integers perm (1-indexed) is considered a beautiful arrangement if
for every i (1 <= i <= n), either of the following is true:

perm[i] is divisible by i.
i is divisible by perm[i].
Given an integer n, return the number of the beautiful arrangements that you can construct.
"""

class Solution:
    def countArrangement(self, n: int) -> int:
        # bottom-up approach (memoized dp)
        cache = [0] * (n+1)
        cache[1], cache[2] = 1, 2
        if n <= 2:
            return cache[n]

        def dp(k):
            idxs = list(range(1, k+1))
            vals = list(range(1, k+1))

            return 

        for i in range(3, n+1):
            cache[i] = cache[i-1] + dp(i)
        return cache[-1]
