"""
59. Spiral Matrix II

Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
"""


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0] * n for _ in range(n)]
        i, j = 0, 0
        right, down = True, True

        for k in range(1, n ** 2 + 1):
            res[i][j] = k
            if right and down:
                if j + 1 < n and res[i][j + 1] == 0:
                    j += 1
                else:
                    right = False
                    i += 1
            elif not right and down:
                if i + 1 < n and res[i + 1][j] == 0:
                    i += 1
                else:
                    down = False
                    j -= 1
            elif not right and not down:
                if j - 1 >= 0 and res[i][j - 1] == 0:
                    j -= 1
                else:
                    right = True
                    i -= 1
            elif right and not down:
                if i - 1 >= 0 and res[i - 1][j] == 0:
                    i -= 1
                else:
                    down = True
                    j += 1
        return res

"""
Runtime: 27 ms, faster than 53.75% of Python online submissions for Spiral Matrix II.
Memory Usage: 13.5 MB, less than 45.64% of Python online submissions for Spiral Matrix II.
"""