class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)


        while(i<n):
            if nums[i] != i + 1 and nums[i] <= n:
                correctIndex = nums[i] - 1

                if nums[i] > 0 and nums[i] != nums[correctIndex]:
                    self.swap(i, correctIndex, nums)
                else:
                    i += 1
            else:
                i += 1
        
        # now iterate through the cyclic sorted array
        for j in range(len(nums)):
            if nums[j] != j + 1:
                return j + 1
        
        return n + 1
    
    def swap(self, i, corr, nums):
        temp = nums[i]
        nums[i] = nums[corr]
        nums[corr] = temp