# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = [0]
        def helper(root, k):
            if root == None:
                return None

            left = helper(root.left, k)

            if left != None:
                return left
            cnt[0] += 1

            if cnt[0] == k:
                return root.val
            
            return helper(root.right, k)
        return helper(root, k)
        
            