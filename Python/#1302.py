"""
1302. Deepest Leaves Sum

Given a binary tree, return the sum of values of its deepest leaves.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if root:
            cur_level = [root]
            while len(cur_level)>0:
                new_level = []
                for leaf in cur_level:
                    if leaf.left:
                        new_level.append(leaf.left)
                    if leaf.right:
                        new_level.append(leaf.right)
                if len(new_level) == 0:
                    break
                cur_level = new_level
            return sum([leaf.val for leaf in cur_level])
        return 0

"""
Runtime: 84 ms, faster than 94.36% of Python3 online submissions for Deepest Leaves Sum.
Memory Usage: 17.8 MB, less than 39.97% of Python3 online submissions for Deepest Leaves Sum.
"""
