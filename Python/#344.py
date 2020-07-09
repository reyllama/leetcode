"""
344. Reverse String

Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place

with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.



Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        while i < len(s)-1:
            if i==0:
                s.append(s[0])
                s.pop(0)
            else:
                s.insert(len(s)-i, s[0])
                s.pop(0)
            i += 1

"""
Runtime: 1156 ms, faster than 5.15% of Python3 online submissions for Reverse String.
Memory Usage: 18.1 MB, less than 95.68% of Python3 online submissions for Reverse String.
"""


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()


"""
Runtime: 284 ms, faster than 12.82% of Python3 online submissions for Reverse String.
Memory Usage: 18.4 MB, less than 23.22% of Python3 online submissions for Reverse String.
"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            t = s[i]
            s[i] = s[len(s)-1-i]
            s[len(s)-1-i] = t

"""
Runtime: 264 ms, faster than 15.35% of Python3 online submissions for Reverse String.
Memory Usage: 18 MB, less than 98.30% of Python3 online submissions for Reverse String.
"""
