# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = [0]
        
        def height(root):
            if root is None:
                return 0

            leftHeight = height(root.left)
            rightHeight = height(root.right)

            dia = leftHeight + rightHeight + 1
            diameter[0] = max(diameter[0], dia)

            return max(leftHeight, rightHeight) + 1
        
        height(root)
        return diameter[0] - 1
