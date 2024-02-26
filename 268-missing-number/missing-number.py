class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)

        while(i<n):
            corrIndex = nums[i]
            if (nums[i] < n and nums[i] != i):
                temp = nums[i]
                nums[i] = nums[corrIndex]
                nums[corrIndex] = temp
            else:
                i += 1
        
        for j in range(len(nums)):
            if j != nums[j]:
                return j
        return n

        