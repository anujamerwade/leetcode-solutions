class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        # if x > 0:
        #     if n > 0:
        #         return self.findPower(x, n)
        #     if n < 0:
        #         return 1/self.findPower(x, abs(n))
        
        # if x < 0:
        #     return self.findPower(x, n)

        if n < 0:
            x = 1 / x
            n = -n

        return self.findPower(x, n)

    
    def findPower(self, x, n):
        if n == 0:
            return 1
        
        if n == 1:
            return x
        
        half = self.findPower(x, n // 2)

        if n % 2 == 0:
            return half * half
        else:
            return half * half * x
        
