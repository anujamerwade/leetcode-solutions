class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = 0
        res = 0

        for n in nums:
            if c == 0:
                res = n
            c += (1 if n == res else - 1)   # add 1 or subtract 1
        return res

        