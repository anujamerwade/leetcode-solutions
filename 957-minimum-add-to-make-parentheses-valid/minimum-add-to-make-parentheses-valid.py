class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []

        for bracket in s:
            if bracket == "(":
                stack.append(bracket)
            elif bracket == ")":
                # it means it is a closing bracket
                if stack and '(' == stack[-1]:
                    stack.pop()
                else:
                    stack.append(bracket)
        return len(stack)
        