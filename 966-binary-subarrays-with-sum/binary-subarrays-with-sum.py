class Solution:

    def slidingWindow(self, nums: List[int], goal: int) -> int:
        start, currSum, totalCount = 0, 0, 0

        for end in range(len(nums)):
            currSum += nums[end]

            while currSum > goal and start <= end:
                currSum -= nums[start]
                start += 1
            
            totalCount += end - start + 1
        return totalCount

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.slidingWindow(nums, goal) - self.slidingWindow(nums, goal-1)