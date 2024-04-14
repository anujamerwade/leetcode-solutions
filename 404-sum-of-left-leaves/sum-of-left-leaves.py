# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def helper(root, leftside):
            if root == None:
                return None

            helper(root.left, True)
            helper(root.right, False)

            if not root.left and not root.right and leftside:
                self.ans += root.val
            return self.ans
        return helper(root, False)

            
        
        
        