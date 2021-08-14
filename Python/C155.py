"""
155. Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
"""

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        import heapq
        from collections import defaultdict
        self.nums = []
        self.heap = []
        self.cnt = defaultdict(int)

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.nums += [val]
        self.cnt[val] += 1
        heapq.heappush(self.heap, val)
        
    def pop(self):
        """
        :rtype: None
        """
        tmp = self.nums.pop()
        self.cnt[tmp] -= 1
        
    def top(self):
        """
        :rtype: int
        """
        return self.nums[-1]

    def getMin(self):
        """
        :rtype: int
        """
        while True:
            if self.cnt[self.heap[0]] > 0:
                return self.heap[0]
            else:
                heapq.heappop(self.heap)
                


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

"""
Runtime: 94 ms, faster than 31.50% of Python online submissions for Min Stack.
Memory Usage: 17.4 MB, less than 25.25% of Python online submissions for Min Stack.
"""