class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = set()
        i = 0
        n = len(nums)

        while i < n:
            if nums[i] != i + 1:
                correctIndex = nums[i] - 1
                if nums[i] != nums[correctIndex]:
                    self.swap(i, correctIndex, nums)
                else:
                    ans.add(nums[i])
                    i += 1
            else:
                i += 1
        
        return list(ans)
    
    def swap(self, i, corr, nums):
        temp = nums[i]
        nums[i] = nums[corr]
        nums[corr] = temp