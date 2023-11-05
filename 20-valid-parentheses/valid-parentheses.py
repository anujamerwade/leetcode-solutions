class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            ')':'(',
            ']':'[',
            '}':'{'
        }

        stack = []

        for bracket in s:
            if bracket in ("{","[","("):
                stack.append(bracket)
            else:
                # it means it is not a closing bracket
                if bracket == ']':
                    if not stack or '[' != stack.pop():
                        return False
                if bracket == ')':
                    if not stack or '(' != stack.pop():
                        return False
                if bracket == '}':
                    if not stack or '{' != stack.pop():
                        return False
        if not stack:
            return True
        else:
            return False



        