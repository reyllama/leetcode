"""
1323. Maximum 69 Number

Given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

"""

class Solution:
    def maximum69Number (self, num: int) -> int:
        s = str(num) + "0"
        for i, v in enumerate(s):
            if v == "6":
                s = s[:i] + "9" + s[i+1:]
                break
        return int(s[:-1])

"""
Runtime: 32 ms, faster than 48.69% of Python3 online submissions for Maximum 69 Number.
Memory Usage: 13.9 MB, less than 98.05% of Python3 online submissions for Maximum 69 Number.
"""
