class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        i = 0

        if k == len(num):
            return "0"

        for i in range(len(num)):
            while k > 0 and stack and num[i] < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(num[i])
        
        # if k is still positive, then remove last k digits from stack
        stack = stack[:len(stack) - k]
        
        ans = "".join(stack)

        # Remove leading zeros
        ans = ans.lstrip('0')

        # If ans is empty after removing leading zeros, return "0"
        if not ans:
            return "0"

        return ans