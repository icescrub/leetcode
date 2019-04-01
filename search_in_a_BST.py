# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root, val):
        if root.val == val:
            return root
        elif root.left is not None and root.val > val:
            return self.searchBST(root.left, val)
        elif root.right is not None and root.val < val:
            return self.searchBST(root.right, val)
        else:
            return []
