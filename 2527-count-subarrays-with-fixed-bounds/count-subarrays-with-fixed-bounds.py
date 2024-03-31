class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        bad = -1
        l, r = -1, -1
        res = 0

        for i in range(len(nums)):
            if not minK <= nums[i] <= maxK:
                bad = i
            if nums[i] == minK:
                l = i
            if nums[i] == maxK:
                    r = i
            res += max(0, min(l, r) - bad)
        return res
# TC: O(n)
# SC: O(n)