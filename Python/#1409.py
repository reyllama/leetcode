"""
1409. Queries on a Permutation With Key

Given the array queries of positive integers between 1 and m, you have to process all queries[i] (from i=0 to i=queries.length-1) according to the following rules:

In the beginning, you have the permutation P=[1,2,3,...,m].
For the current i, find the position of queries[i] in the permutation P (indexing from 0) and then move this at the beginning of the permutation P. Notice that the position of queries[i] in P is the result for queries[i].
Return an array containing the result for the given queries.
"""

class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:

        out = []
        per = [_ for _ in range(1, m+1)]

        for q in queries:
            idx = per.index(q)
            if idx < m-1:
                per = [per[idx]] + per[:idx] + per[idx+1:]
            else:
                per = [per[idx]] + per[:idx]
            out.append(idx)

        return out

"""
Runtime: 80 ms, faster than 34.82% of Python3 online submissions for Queries on a Permutation With Key.
Memory Usage: 14.4 MB, less than 84.58% of Python3 online submissions for Queries on a Permutation With Key.
"""
