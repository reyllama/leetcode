"""
1431. Kids With the Greatest Number of Candies


Given the array candies and the integer extraCandies, where candies[i] represents the number of candies that the ith kid has.

For each kid check if there is a way to distribute extraCandies among the kids such that he or she can have the greatest number of candies among them.
Notice that multiple kids can have the greatest number of candies.
"""

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        M = max(candies)
        return [candy+extraCandies >= M for candy in candies]

"""
Runtime: 28 ms, faster than 98.79% of Python3 online submissions for Kids With the Greatest Number of Candies.
Memory Usage: 14.2 MB, less than 82.38% of Python3 online submissions for Kids With the Greatest Number of Candies.
"""
