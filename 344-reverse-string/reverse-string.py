class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s) - 1

        return self.reversal(s, l, r)

    def reversal(self, s, l, r):
        if l <= r:
            temp = s[l]
            s[l] = s[r]
            s[r] = temp


            return self.reversal(s, l+1, r-1)

            
        else:
            pass
        