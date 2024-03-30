class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.slidingWindowAtMost(nums, k) - self.slidingWindowAtMost(nums, k - 1)

    def slidingWindowAtMost(self, nums, k):
        freq = Counter()
        l, count = 0, 0

        for r in range(len(nums)):
            freq[nums[r]] += 1

            while len(freq) > k:
                freq[nums[l]] -= 1
                if freq[nums[l]] == 0:
                    del freq[nums[l]]
                l += 1
            count += (r - l + 1)
        return count
