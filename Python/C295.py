"""
295. Find Median from Data Stream

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
"""
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        from heapq import *
        self.l = []
        self.r = []
        
        
    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        
        if len(self.l)==len(self.r):
            heappush(self.r, -heappushpop(self.l, -num))
        else:
            heappush(self.l, -heappushpop(self.r, num))
        
    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.l)==len(self.r):
            return (self.r[0]-self.l[0])/2.0
        else:
            return self.r[0]
        
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

"""
Runtime: 1060 ms, faster than 28.31% of Python online submissions for Find Median from Data Stream.
Memory Usage: 38.3 MB, less than 21.16% of Python online submissions for Find Median from Data Stream.
"""