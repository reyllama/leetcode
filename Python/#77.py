"""
77. Combinations

Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

You may return the answer in any order.
"""

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(arr):
            if len(arr)==k:
                res.append(list(arr))
                return
            start = arr[-1]+1 if arr else 1
            for i in range(start, n+1):
                arr.append(i)
                dfs(arr)
                arr.pop()
        dfs([])
        return res

"""
Runtime: 543 ms, faster than 50.60% of Python3 online submissions for Combinations.
Memory Usage: 16 MB, less than 18.88% of Python3 online submissions for Combinations.
"""