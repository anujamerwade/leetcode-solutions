class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dups = set()
        if len(nums) < 2:
            return False
        for num in nums:
            if num not in dups:
                dups.add(num)
            else:
                return True
        return False
