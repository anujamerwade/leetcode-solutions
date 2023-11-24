class Solution:
    def isHappy(self, n: int) -> bool:

        visited = set()
        ans = n

        while True:
            ans = self.findSquares(ans)
            if ans == 1:
                return True
            if ans not in visited:
                visited.add(ans)
            else:
                return False

        # fast, slow = n, n
        
        # while True:
        #     slow = self.findSquares(slow)
        #     fast = self.findSquares(self.findSquares(fast))
        #     if slow == fast:
        #         break
  
        # return slow == 1

    
    def findSquares(self, num):
        ans = 0

        while num != 0:
            ans += (num%10)**2
            num //= 10
        return ans
        