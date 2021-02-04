"""
1689. Partitioning Into Minimum Number Of Deci-Binary Numbers

A decimal number is called deci-binary if each of its digits is either 0 or 1 without any leading zeros.
For example, 101 and 1100 are deci-binary, while 112 and 3001 are not.

Given a string n that represents a positive decimal integer,
return the minimum number of positive deci-binary numbers needed so that they sum up to n.
"""

class Solution:
    def minPartitions(self, n: str) -> int:
        return max([int(d) for d in n])

"""
Runtime: 216 ms, faster than 32.10% of Python3 online submissions for Partitioning Into Minimum Number Of Deci-Binary Numbers.
Memory Usage: 16.3 MB, less than 6.07% of Python3 online submissions for Partitioning Into Minimum Number Of Deci-Binary Numbers.
"""

class Solution:
    def minPartitions(self, n: str) -> int:
        M = 0
        for s in n:
            if s=="9":
                return 9
            if int(s) > M:
                M = s
        return M

"""
Runtime: 180 ms, faster than 52.09% of Python3 online submissions for Partitioning Into Minimum Number Of Deci-Binary Numbers.
Memory Usage: 14.6 MB, less than 88.07% of Python3 online submissions for Partitioning Into Minimum Number Of Deci-Binary Numbers.
"""
