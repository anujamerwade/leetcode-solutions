class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        hare = 0
        tortoise = 0

        # detect cycle
        while True:
            hare = nums[nums[hare]]
            tortoise = nums[tortoise]
            if hare == tortoise:
                break

        tortoise = 0
        while True:
            hare = nums[hare]
            tortoise = nums[tortoise]
            if hare == tortoise:
                return hare

