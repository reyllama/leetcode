"""
149. Max Points on a Line

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.
"""


class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        maxi = 0
        for i, point in enumerate(points[:-1]):
            cnts = defaultdict(int)

            for j, point_ in enumerate(points[i + 1:]):
                slope = (point[1] - point_[1]) / (point[0] - point_[0]) if (point[0] - point_[0]) != 0 else 'v'
                cnts[slope] += 1

            print(point, cnts)

            cur_max = max(cnts.values())
            maxi = max(cur_max, maxi)
        return maxi + 1

"""
Runtime: 130 ms, faster than 64.63% of Python3 online submissions for Max Points on a Line.
Memory Usage: 14.4 MB, less than 40.37% of Python3 online submissions for Max Points on a Line.
"""