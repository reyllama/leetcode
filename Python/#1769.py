"""
1769. Minimum Number of Operations to Move All Balls to Each Box

You have n boxes. You are given a binary string boxes of length n, where boxes[i] is '0' if the ith box is empty, and '1' if it contains one ball.

In one operation, you can move one ball from a box to an adjacent box. Box i is adjacent to box j if abs(i - j) == 1. Note that after doing so, there may be more than one ball in some boxes.

Return an array answer of size n, where answer[i] is the minimum number of operations needed to move all the balls to the ith box.

Each answer[i] is calculated considering the initial state of the boxes.

 """

# class Solution:
#    def minOperations(self, boxes: str) -> List[int]:
#
#        out = [sum([abs(i-j)*int(v) for i, v in enumerate(boxes)]) for j in range(len(boxes))]
#
#        return out

"""
Time Limit Exceeded
"""
#
# class Solution:
#     def minOperations(self, boxes: str) -> List[int]:
#
#         n = len(boxes)
#         out = []
#         boxes = "0"*n + boxes + "0"*n
#         for i in range(0, n):
#             c = 0
#             for j in range(1, n):
#                 c += j*(int(boxes[n+i-j])+int(boxes[n+i+j]))
#             out.append(c)
#         return out
"""
Time Limit Exceeded
"""


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # O(n)
        n = len(boxes)
        out = [0]*n # zero-pad

        # Look to your right
        cur, step = 0, 0
        for i in range(n):
            out[i] += step
            if boxes[i] == '1':
                cur += 1
            step += cur # all 1 values to your left are enlarged by 1 (step)

        # Look to your left
        cur, step = 0, 0
        for i in reversed(range(n)):
            out[i] += step
            if boxes[i] == '1':
                cur += 1
            step += cur

        return out

"""
Runtime: 68 ms, faster than 100.00% of Python3 online submissions for Minimum Number of Operations to Move All Balls to Each Box.
Memory Usage: 14.7 MB, less than 33.33% of Python3 online submissions for Minimum Number of Operations to Move All Balls to Each Box.
"""
