class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s = 0
        e = len(nums) - 1

        return self.recursiveSearch(nums, target, s, e)
    
    def recursiveSearch(self, nums, target, s, e):
        m = s + (e-s)//2

        if nums[m] == target:
            return m
        
        if s<= e:
            if nums[s] <= nums[m]:    # left sorted array
                if (target <= nums[m] and target >= nums[s]):
                    return self.recursiveSearch(nums, target, s, m - 1)
                else:
                    return self.recursiveSearch(nums, target, m + 1, e)
                    
                    
            else:
                if (target >= nums[m] and target <= nums[e]):
                    return self.recursiveSearch(nums, target, m + 1, e)
                else:
                    return self.recursiveSearch(nums, target, s, m-1)
        else:
            return -1