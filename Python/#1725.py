"""
1725. Number Of Rectangles That Can Form The Largest Square

You are given an array rectangles where rectangles[i] = [li, wi] represents the ith rectangle of length li and width wi.

You can cut the ith rectangle to form a square with a side length of k if both k <= li and k <= wi. For example, if you have a rectangle [4,6], you can cut it to get a square with a side length of at most 4.

Let maxLen be the side length of the largest square you can obtain from any of the given rectangles.

Return the number of rectangles that can make a square with a side length of maxLen.
"""

class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:

        cur, cnt = 0, 0

        for rec in rectangles:
            m = min(rec)
            if m > cur:
                cur = m
                cnt = 1
            elif m == cur:
                cnt += 1

        return cnt

"""
Runtime: 172 ms, faster than 98.52% of Python3 online submissions for Number Of Rectangles That Can Form The Largest Square.
Memory Usage: 15 MB, less than 39.82% of Python3 online submissions for Number Of Rectangles That Can Form The Largest Square.
"""
