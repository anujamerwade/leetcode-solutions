class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []

        s = 0
        e = len(nums) - 1

        while s <= e:
            if nums[s]*nums[s] < nums[e]*nums[e]:
                ans.append(nums[e]*nums[e])
                e -= 1
            else:
                ans.append(nums[s]*nums[s])
                s += 1

        
        return ans[::-1] # reversed
        