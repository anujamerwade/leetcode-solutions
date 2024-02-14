class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = [None]*len(nums)
        pos = 0
        neg = 1

        for num in nums:
            if num > 0:
                ans[pos] = num
                if pos < len(nums)-1:
                    pos += 2
            else:
                ans[neg] = num
                if neg < len(nums):
                    neg += 2
        return ans