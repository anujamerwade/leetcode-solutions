# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        ans = []

        reverse = False

        if not root:
            return ans
        
        q.append(root)

        while q:
            levelNodes = []  # List to store node values at the current level
            for _ in range(len(q)):
                if not reverse:
                    currNode = q.popleft()
                    levelNodes.append(currNode.val)
                    if currNode.left:
                        q.append(currNode.left)
                    if currNode.right:
                        q.append(currNode.right)
                else:
                    currNode = q.pop()
                    levelNodes.append(currNode.val)
                    if currNode.right:
                        q.insert(0, currNode.right)
                    if currNode.left:
                        q.insert(0, currNode.left)

            reverse = not reverse
            ans.append(levelNodes)
        
        return ans