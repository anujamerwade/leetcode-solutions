class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []

        hs1 = set(nums1)
        hs2 = set(nums2)

        if len(hs1) <= len(hs2):
            for num in hs1:
                if num in hs2:
                    res.append(num)
        else:
            for num in hs2:
                if num in hs1:
                    res.append(num)
        return res