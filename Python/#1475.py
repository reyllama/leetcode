"""
1475. Final Prices With a Special Discount in a Shop

Given the array prices where prices[i] is the price of the ith item in a shop. There is a special discount for items in the shop, if you buy the ith item, then you will receive a discount equivalent to prices[j] where j is the minimum index such that j > i and prices[j] <= prices[i], otherwise, you will not receive any discount at all.

Return an array where the ith element is the final price you will pay for the ith item of the shop considering the special discount.
"""

class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        ans = []
        for i, price in enumerate(prices[:-1]):
            on = True
            for j, ref_price in enumerate(prices[i+1:]):
                if ref_price <= price:
                    ans.append(price-ref_price)
                    on = False
                    break
            if on == True:
                ans.append(price)
        ans += prices[-1:]
        return ans

"""
Runtime: 52 ms, faster than 54.73% of Python online submissions for Final Prices With a Special Discount in a Shop.
Memory Usage: 13.6 MB, less than 36.63% of Python online submissions for Final Prices With a Special Discount in a Shop.
"""