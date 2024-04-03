# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q = deque([(root, None)])

        if not root:
            return False
        
        while q:
            levelSize = len(q)
            foundX, foundY = False, False
            parentX, parentY = None, None

            for _ in range(levelSize):
                node, parent = q.popleft()

                if node.val == x:
                    foundX = True
                    parentX = parent
                elif node.val == y:
                    foundY = True
                    parentY = parent
                
                if node.left:
                    q.append((node.left, node))
                if node.right:
                    q.append((node.right, node))
        
            if foundX and foundY and parentX != parentY:
                return True
        
        return False