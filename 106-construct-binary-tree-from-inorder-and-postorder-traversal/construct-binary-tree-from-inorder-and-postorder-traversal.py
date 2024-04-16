# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        if len(postorder) == 0 or len(inorder) == 0:
            return None

        root = postorder.pop()
        # index = 0

        # for i in range(len(inorder)):
        #     if inorder[i] == root:
        #         index = i

        node = TreeNode(root)
        index = inorder.index(root)

        node.right = self.buildTree(inorder[index+1:], postorder)
        node.left = self.buildTree(inorder[:index], postorder)

        return node