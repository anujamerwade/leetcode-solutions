class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxEle = max(nums)
        ans, start = 0, 0
        maxEleinWindow = 0

        for end in range(len(nums)):
            if nums[end] == maxEle:
                maxEleinWindow += 1
            
            while maxEleinWindow == k:
                if nums[start] == maxEle:
                    maxEleinWindow -= 1
                start += 1
            
            ans += start
        return ans
                    
