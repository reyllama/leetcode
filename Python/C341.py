"""
341. Flatten Nested List Iterator

You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.

Implement the NestedIterator class:

NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list nestedList.
int next() Returns the next integer in the nested list.
boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.
Your code will be tested with the following pseudocode:

initialize iterator with nestedList
res = []
while iterator.hasNext()
    append iterator.next() to the end of res
return res

If res matches the expected flattened list, then your code will be judged as correct.
"""

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        
        self.arr = []
        
        def flatten(arr):
            out = []
            for v in arr.getList():
                if v.isInteger():
                    out.append(v.getInteger())
                else:
                    out += flatten(v)
            return out
        
        for v in nestedList:
            if v.isInteger():
                self.arr += [v.getInteger()]
            else:
                self.arr += flatten(v)
        
        self.arr = self.arr[::-1]
    
    def next(self):
        """
        :rtype: int
        """
        return self.arr.pop()

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.arr)>0

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

"""
Runtime: 64 ms, faster than 88.00% of Python online submissions for Flatten Nested List Iterator.
Memory Usage: 19 MB, less than 79.56% of Python online submissions for Flatten Nested List Iterator.
"""