class Solution:
    def isHappy(self, n: int) -> bool:

        fast, slow = n, n

        # slow = self.findSquares(slow)
        # fast = self.findSquares(self.findSquares(fast))
        
        while True:
            slow = self.findSquares(slow)
            fast = self.findSquares(self.findSquares(fast))
            if slow == fast:
                break
  
        return slow == 1

    
    def findSquares(self, num):
        ans = 0

        while num != 0:
            ans += (num%10)**2
            num //= 10
        return ans
        