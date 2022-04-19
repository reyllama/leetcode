"""
1387. Sort Integers by The Power Value

The power of an integer x is defined as the number of steps needed to transform x into 1 using the following steps:

    if x is even then x = x / 2
    if x is odd then x = 3 * x + 1

For example, the power of x = 3 is 7 because 3 needs 7 steps to become 1 (3 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1).

Given three integers lo, hi and k. The task is to sort all integers in the interval [lo, hi] by the power value in ascending order, if two or more integers have the same power value sort them by ascending order.

Return the kth integer in the range [lo, hi] sorted by the power value.

Notice that for any integer x (lo <= x <= hi) it is guaranteed that x will transform into 1 using these steps and that the power of x is will fit in a 32-bit signed integer.
"""

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        # memoization
        # self.cache = dict()
        
        def dp(num, cur):
            if num==1:
                return cur
            # elif self.cache.get(num, False):
            #     return cur + self.cahce[num]
            elif num % 2 == 0:
                return dp(num//2, cur+1)
            else:
                return dp(3*num+1, cur+1)
            
        res = dict()
        for n in range(lo, hi+1):
            res[n] = dp(n, 0)
            
        res = {k:v for k, v in sorted(res.items(), key=lambda x: x[1])}
            
        return list(res.keys())[k-1]

"""
Runtime: 842 ms, faster than 33.56% of Python3 online submissions for Sort Integers by The Power Value.
Memory Usage: 14.3 MB, less than 38.62% of Python3 online submissions for Sort Integers by The Power Value.
"""
