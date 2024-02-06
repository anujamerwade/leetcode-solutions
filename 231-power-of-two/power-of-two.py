class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        if n == 0:
            return False
        return self.findPower(n)
    
    def findPower(self, n):
        if n%2 == 0:
            if n//2 == 1:
                return True
            else:
                return self.findPower(n//2)
        else:
            return False