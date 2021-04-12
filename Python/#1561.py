"""
1561. Maximum Number of Coins You Can Get

There are 3n piles of coins of varying size, you and your friends will take piles of coins as follows:

In each step, you will choose any 3 piles of coins (not necessarily consecutive).
Of your choice, Alice will pick the pile with the maximum number of coins.
You will pick the next pile with maximum number of coins.
Your friend Bob will pick the last pile.
Repeat until there are no more piles of coins.
Given an array of integers piles where piles[i] is the number of coins in the ith pile.

Return the maximum number of coins which you can have.


"""

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles = sorted(piles)[::-1]
        n = int(len(piles)*2/3)
        return sum([piles[i] for i in range(n) if i % 2 == 1])

"""
Runtime: 592 ms, faster than 74.15% of Python3 online submissions for Maximum Number of Coins You Can Get.
Memory Usage: 26.5 MB, less than 50.53% of Python3 online submissions for Maximum Number of Coins You Can Get.
"""
