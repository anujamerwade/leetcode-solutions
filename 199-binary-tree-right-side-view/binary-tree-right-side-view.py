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
            n = len(q)
            for i in range(n):
                currNode = q.popleft()
                if currNode.left:
                    q.append(currNode.left)
                if currNode.right:
                    q.append(currNode.right)
                if i == n - 1:
                    ans.append(currNode.val)
            # ans.append(levelNodes[-1])
        
        return ans