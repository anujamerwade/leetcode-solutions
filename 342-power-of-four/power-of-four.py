class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        if n < 4:
            return False
        if n % 4 != 0:
            return False
        else:
            # number could be a power of 4
            return self.isPowerOfFour(n//4)
    
    # def findPower(self, n):
    #     if n%4 == 0:
    #         if n//4 == 1:
    #             return True
    #         else:
    #             return self.findPower(n//4)
    #     else:
    #         return False
        
        