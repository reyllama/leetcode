"""
1282. Group the People Given the Group Size They Belong To

There are n people whose IDs go from 0 to n - 1 and each person belongs exactly to one group. Given the array groupSizes of length n telling the group size each person belongs to, return the groups there are and the people's IDs each group includes.

You can return any solution in any order and the same applies for IDs. Also, it is guaranteed that there exists at least one solution.



Example 1:

Input: groupSizes = [3,3,3,3,3,1,3]
Output: [[5],[0,1,2],[3,4,6]]
Explanation:
Other possible solutions are [[2,1,6],[5],[0,4,3]] and [[5],[0,6,2],[4,3,1]].

Example 2:

Input: groupSizes = [2,1,3,3,3,2]
Output: [[1],[0,5],[2,3,4]]


Constraints:

groupSizes.length == n
1 <= n <= 500
1 <= groupSizes[i] <= n

"""

class Solution:
    def groupThePeople(self, groupSizes):
        ans = []
        dump = set()
        for idx in range(len(groupSizes)):
            if idx not in dump:
                cur, temp = idx, [idx]
                dump.add(idx)
                # print('idx: ', idx)
                for _ in range(groupSizes[idx]-1):
                    j = groupSizes[cur+1:].index(groupSizes[idx])+cur+1
                    # print('j: ', j)
                    temp.append(j)
                    dump.add(j)
                    cur = j
                ans.append(temp)
        return ans

"""
Runtime: 116 ms, faster than 20.75% of Python3 online submissions for Group the People Given the Group Size They Belong To.
Memory Usage: 14 MB, less than 27.35% of Python3 online submissions for Group the People Given the Group Size They Belong To.
"""

from collections import defaultdict
class Solution:
    def groupThePeople(self, groupSizes):
        d, ans = defaultdict(list), []
        for i, v in enumerate(groupSizes):
            d[v].append(i)
            if len(d[v])%v == 0:
                ans.append(d[v])
                d[v] = []
        return ans

"""
Runtime: 84 ms, faster than 53.89% of Python3 online submissions for Group the People Given the Group Size They Belong To.
Memory Usage: 13.8 MB, less than 72.65% of Python3 online submissions for Group the People Given the Group Size They Belong To.
"""

x = Solution()
print(x.groupThePeople([3,3,3,3,3,1,3]))
