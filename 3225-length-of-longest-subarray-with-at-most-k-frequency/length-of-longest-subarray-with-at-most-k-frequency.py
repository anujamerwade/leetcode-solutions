class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = Counter()
        start = -1       
        length = 0

        for end in range(len(nums)):
            freq[nums[end]] += 1

            while freq[nums[end]] > k:
                start += 1
                freq[nums[start]] -= 1
            length = max(length, end - start)

        return length       
        