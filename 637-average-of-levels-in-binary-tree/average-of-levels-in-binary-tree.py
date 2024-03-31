# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque()
        ans = []

        if not root:
            return ans
        
        q.append(root)

        while q:
            sumNodes = 0
            size = len(q)
            # levelNodes = []  # List to store node values at the current level
            for _ in range(len(q)):
                currNode = q.popleft()
                # levelNodes.append(currNode.val)
                sumNodes += currNode.val
                if currNode.left:
                    q.append(currNode.left)
                if currNode.right:
                    q.append(currNode.right)
            ans.append(sumNodes/size)
        
        return ans
# TC: O(n)
# SC: O(n)