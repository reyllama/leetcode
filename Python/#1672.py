"""
1672. Richest Customer Wealth

You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.
"""

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(accounts[i]) for i in range(len(accounts))])


# class Solution:
#     def maximumWealth(self, accounts: List[List[int]]) -> int:
#         cur_max = 0
#         for i in range(len(accounts)):
#             t = sum(accounts[i])
#             if t > cur_max:
#                 cur_max = t
#         return cur_max

"""
Runtime: 56 ms, faster than 48.37% of Python3 online submissions for Richest Customer Wealth.
Memory Usage: 14.3 MB, less than 29.34% of Python3 online submissions for Richest Customer Wealth.
"""
