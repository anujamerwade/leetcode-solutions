class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:

        i, j = 0, 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums2[j] < nums1[i]:
                j += 1
            else:
                # both are equal
                return nums1[i]
        return -1
# TC: O(n)
# SC: O(1)