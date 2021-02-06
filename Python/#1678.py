"""
1678. Goal Parser Interpretation

You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.

Given the string command, return the Goal Parser's interpretation of command.
"""

class Solution:
    def interpret(self, command):
        return command.replace("()", "o").replace("(al)", "al")

"""
Runtime: 24 ms, faster than 95.66% of Python3 online submissions for Goal Parser Interpretation.
Memory Usage: 14.2 MB, less than 73.51% of Python3 online submissions for Goal Parser Interpretation.
"""
