class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        count = 0
        return self.helper(num1, num2, count)
    
    def helper(self, num1, num2, count):
        if num1 == 0 or num2 == 0:
            return count
        if num1 < num2:
            count += 1
            return self.helper(num1, num2-num1, count)
        else:
            count += 1
            return self.helper(num1-num2, num2, count)