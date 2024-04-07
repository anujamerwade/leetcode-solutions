class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        memo = [[-1] * n for _ in range(n)]
        return self.isValidString(0, 0, s, memo)
    
    def isValidString(self, index, open, s, memo):
        if index == len(s):
            return open == 0

        if memo[index][open] != -1:
            # result is computed
            return memo[index][open] == 1

        isValid = False

        if s[index] == "*":
            # try all possibilities

            # * as (
            isValid |= self.isValidString(index + 1, open+1, s, memo)

            if open > 0:
                # * as )
                isValid |= self.isValidString(index + 1, open-1, s, memo)
            
            # * is ""
            isValid |= self.isValidString(index + 1, open, s, memo)
        else:
            # handle ( or )
            if s[index] == '(':
                isValid = self.isValidString(index + 1, open+1, s, memo)
            elif open > 0:
                isValid |= self.isValidString(index + 1, open-1, s, memo)

        # Memoize and return the result
        memo[index][open] = 1 if isValid else 0
        return isValid