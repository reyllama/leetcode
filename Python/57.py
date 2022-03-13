"""
57. Insert Interval

You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.
"""

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if len(intervals)==0:
            return [newInterval]

        s, e = newInterval
        starts, ends, Lidx, Ridx = [s], [e], [], []
        res = []

        for i, itv in enumerate(intervals):
            si, ei = itv[0], itv[1]
            if si <= e and ei >= s:
                starts.append(si)
                ends.append(ei)
                
            if ei < s:
                Lidx.append(i)
            if si > e:
                Ridx.append(i)

        if Lidx:
            res += intervals[:Lidx[-1]+1]
        res.append([min(starts), max(ends)])
        if Ridx:
            res += intervals[Ridx[0]:]

        return res

"""
Runtime: 68 ms, faster than 74.93% of Python online submissions for Insert Interval.
Memory Usage: 16.9 MB, less than 21.21% of Python online submissions for Insert Interval.
"""

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
# intervals = [[1,5]]
# newInterval = [6,8]
s = Solution()
res = s.insert(intervals, newInterval)
print(res)