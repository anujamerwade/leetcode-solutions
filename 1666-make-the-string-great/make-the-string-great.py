class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        
        for ch in s:
            if stack and abs(ord(stack[-1]) - ord(ch)) == 32:
                stack.pop()
            else:
                stack.append(ch)
        
        if not stack:
            return ""
        else:
            ans = ""
            for ch in stack:
                ans += ch
            return ans