"""
101. Symmetric Tree

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        base = [root]

        while base:
            cur = []
            dumm = [] # Keep the indices of dummy placeholders (originally None, but we have to append something to preserve the structure)
            for node in base:
                if node.left:
                    cur += [node.left]
                else: # Still need a placeholder to preserve structure (to check symmetry)
                    cur += [TreeNode(val=-101)]
                    dumm += [len(cur)-1]
                if node.right:
                    cur += [node.right]
                else:
                    cur += [TreeNode(val=-101)]
                    dumm += [len(cur)-1]
            for i in range(len(cur)//2):
                if cur[i].val != cur[len(cur)-i-1].val: # Symmetry has been violated
                    return False
            for i in dumm[::-1]: # Delete from last to first in order to keep the indices straight
                del cur[i]
            base = cur
        return True

"""
Runtime: 20 ms, faster than 80.14% of Python online submissions for Symmetric Tree.
Memory Usage: 13.4 MB, less than 93.65% of Python online submissions for Symmetric Tree.
"""