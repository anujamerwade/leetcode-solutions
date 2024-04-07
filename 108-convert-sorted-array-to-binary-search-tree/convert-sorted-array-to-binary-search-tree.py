# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.sortedArr(nums, 0, len(nums))

    def sortedArr(self, nums, s, e):
        if s >= e:
            return None
        
        mid = s + (e-s)//2

        root = TreeNode(nums[mid])
        root.left = self.sortedArr(nums, s, mid)
        root.right = self.sortedArr(nums, mid + 1, e)
        
        return root