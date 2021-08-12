"""
121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = set()
        curMin, curMax = 10**4, 0
        for price in prices:
            if price < curMin:
                res.add(curMax-curMin)
                curMin = price
                curMax = price
            if price > curMax:
                curMax = price
        res.add(curMax-curMin)
        return max(res)

"""
Runtime: 804 ms, faster than 92.54% of Python online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 22.7 MB, less than 54.57% of Python online submissions for Best Time to Buy and Sell Stock.
"""