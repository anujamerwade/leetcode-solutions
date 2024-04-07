# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0

        leftHeight = self.minDepth(root.left)
        rightHeight = self.minDepth(root.right)

        if leftHeight != 0 and rightHeight != 0:
            return min(leftHeight, rightHeight) + 1
        elif leftHeight == 0:
            return rightHeight + 1
        else:
            return leftHeight + 1