"""
1315. Sum of Nodes with Even-Valued Grandparent

Given a binary tree, return the sum of values of nodes with even-valued grandparent.  (A grandparent of a node is the parent of its parent, if it exists.)

If there are no nodes with an even-valued grandparent, return 0.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        # Helper Function
        def get_sums(node):
            res = 0
            v1, v2, v3, v4 = 0,0,0,0
            v1 += node.left.left.val if node.left and node.left.left else 0
            v2 += node.left.right.val if node.left and node.left.right else 0
            v3 += node.right.left.val if node.right and node.right.left else 0
            v4 += node.right.right.val if node.right and node.right.right else 0
            return v1+v2+v3+v4
        ans = 0
        # Level Traversal
        if root:
            cur_level = [root]
            while len(cur_level) > 0:
                new_level, vals = [], []
                for node in cur_level:
                    if node.val % 2 == 0:
                        ans += get_sums(node)
                    if node.left:
                        new_level.append(node.left)
                    if node.right:
                        new_level.append(node.right)
                cur_level = new_level
        return ans

"""
Runtime: 100 ms, faster than 68.10% of Python3 online submissions for Sum of Nodes with Even-Valued Grandparent.
Memory Usage: 17.6 MB, less than 93.32% of Python3 online submissions for Sum of Nodes with Even-Valued Grandparent.
"""
