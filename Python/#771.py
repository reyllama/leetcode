"""
771. Jewels and Stones

You're given strings jewels representing the types of stones that are jewels,
and stones representing the stones you have. Each character in stones is a type of stone you have.
You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

 """

 class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        c = 0
        for d in stones:
            if d in jewels:
                c += 1
        return c

"""
Runtime: 24 ms, faster than 95.97% of Python3 online submissions for Jewels and Stones.
Memory Usage: 14.2 MB, less than 48.31% of Python3 online submissions for Jewels and Stones.
"""
