"""
1381. Design a Stack With Increment Operation

Design a stack which supports the following operations.

Implement the CustomStack class:

CustomStack(int maxSize) Initializes the object with maxSize which is the maximum number of elements in the stack or do nothing if the stack reached the maxSize.
void push(int x) Adds x to the top of the stack if the stack hasn't reached the maxSize.
int pop() Pops and returns the top of stack or -1 if the stack is empty.
void inc(int k, int val) Increments the bottom k elements of the stack by val. If there are less than k elements in the stack, just increment all the elements in the stack.
"""

class CustomStack:

    def __init__(self, maxSize: int):

        self.mx = maxSize
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.mx:
            self.stack.append(x)

    def pop(self) -> int:
        if len(self.stack)>0:
            return self.stack.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(k):
            if len(self.stack) > i:
                self.stack[i] += val



# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)

# x = [1,2,3,4]
# print(x.pop())
# print(x)
