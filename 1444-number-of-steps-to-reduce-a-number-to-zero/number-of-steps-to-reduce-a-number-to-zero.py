class Solution:
    def numberOfSteps(self, num: int) -> int:
        c = 0
        return self.helper(num, c)
        
    def helper(self, num, c):
        if num == 0:
            return c
        if num % 2 == 0:
            # even number
            num /= 2
            c += 1
        else:
            num -= 1
            c += 1
        return self.helper(num, c)

        