# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        ans = []

        if not root:
            return ans
        
        q.append(root)

        while q:
            levelNodes = []  # List to store node values at the current level
            for _ in range(len(q)):
                currNode = q.popleft()
                levelNodes.append(currNode.val)
                if currNode.left:
                    q.append(currNode.left)
                if currNode.right:
                    q.append(currNode.right)
            ans.append(levelNodes[-1])
        
        return ans