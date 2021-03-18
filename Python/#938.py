"""
938. Range Sum of BST

Given the root node of a binary search tree, return the sum of values of all nodes with a value in the range [low, high].

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""

class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        global out
        out = 0
        def in_order_trav(root):
            if root is None:
                pass
            else:
                if root.val < low:
                    try:
                        in_order_trav(root.right)
                    except:
                        pass
                elif root.val > high:
                    try:
                        in_order_trav(root.left)
                    except:
                        pass
                else:
                    global out
                    out += root.val
                    try:
                        in_order_trav(root.left)
                    except:
                        pass
                    try:
                        in_order_trav(root.right)
                    except:
                        pass
        in_order_trav(root)
        return out

"""
Runtime: 200 ms, faster than 87.85% of Python3 online submissions for Range Sum of BST.
Memory Usage: 22.2 MB, less than 63.31% of Python3 online submissions for Range Sum of BST.
"""
