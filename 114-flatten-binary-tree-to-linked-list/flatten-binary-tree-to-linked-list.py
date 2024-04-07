# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return

        q = deque()

        def traversal(root):
            if root == None:
                return
            q.append(root)
            traversal(root.left)
            traversal(root.right)
            
        traversal(root)

        while q:
            node = q.popleft()
            node.left = None
            if q:
                node.right = q[0]
            else:
                node.right = None
