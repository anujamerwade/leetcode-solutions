class Solution:
    def pivotInteger(self, n: int) -> int:
        totalSum = 0

        for i in range(1, n+1):
            totalSum += i
        
        
        for i in range(1, n+1):
            j = 1
            currSum = 0

            while j <= i:
                currSum += j
                j += 1
            
            if currSum == totalSum - currSum + i:
                # found pivot
                return i
        return -1