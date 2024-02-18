class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def backtrack(path, i):
            if i == len(nums):
                ans.append(path[:])
                return

            # all subsets that include nums[i]
            path.append(nums[i])
            backtrack(path, i+1)
            path.pop()

            # all subsets that do not include nums[i]
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(path, i+1)
        ans = []

        backtrack([], 0)
        return ans