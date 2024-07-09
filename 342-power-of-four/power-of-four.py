class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        if n < 4:
            return False
        return self.findPower(n)
    
    def findPower(self, n):
        if n%4 == 0:
            if n//4 == 1:
                return True
            else:
                return self.findPower(n//4)
        else:
            return False
        
        