class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        steps = 0
        
        while sum(nums) != 0:
            mini = sys.maxsize
            for i in range(len(nums)):
                if nums[i] < mini and nums[i] != 0:
                    mini = nums[i]
            # print(mini)
            
            for i in range(len(nums)):
                if nums[i] != 0:
                    nums[i] -= mini
            # print(nums)
                
            steps += 1
        
        return steps

            