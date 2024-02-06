class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        if n <= 0 or n == 2:
            return False
        return self.findPower(n)
    
    def findPower(self, n):
        if n%3 == 0:
            if n//3 == 1:
                return True
            else:
                return self.findPower(n//3)
        else:
            return False
        