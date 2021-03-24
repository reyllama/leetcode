"""
1732. Find the Highest Altitude

There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.
"""


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max, cur = 0, 0
        for delta in gain:
            cur += delta
            if cur > max:
                max = cur
        return max

"""
Runtime: 32 ms, faster than 88.13% of Python3 online submissions for Find the Highest Altitude.
Memory Usage: 14.2 MB, less than 72.00% of Python3 online submissions for Find the Highest Altitude.
"""
