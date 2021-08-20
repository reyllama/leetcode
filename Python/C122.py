"""
122. Best Time to Buy and Sell Stock II

You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ans, prev = 0, prices[0]
        
        for price in prices[1:]:
            if price > prev:
                ans += (price-prev)
            prev = price
            
        return ans

"""
Runtime: 40 ms, faster than 89.25% of Python online submissions for Best Time to Buy and Sell Stock II.
Memory Usage: 14.4 MB, less than 89.97% of Python online submissions for Best Time to Buy and Sell Stock II.
"""