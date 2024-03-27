class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        c = 0
        prod = 1

        if k <= 1:  # If k is less than or equal to 1, there won't be any subarray with product less than k
            return 0

        l = 0
        for r in range(n):
            prod *= nums[r]
            
            while prod >= k:
                # shrink window from left
                prod /= nums[l]
                l += 1
            
            c += r - l + 1

        return c