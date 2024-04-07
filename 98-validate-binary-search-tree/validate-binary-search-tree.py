# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.checkBST(root, float('-inf'), float('inf'))
    
    def checkBST(self, node, low, high):
        if node is None:
            return True
        
        if (low != None and node.val <= low) or (high!= None and node.val >= high):
            return False

        left = self.checkBST(node.left, low, node.val)
        right = self.checkBST(node.right, node.val, high)
        
        return left and right
        