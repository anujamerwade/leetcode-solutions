class Solution:
    def minInsertions(self, s: str) -> int:
        stack = []
        i = 0
        c = 0

        while i < len(s):
            if s[i] == "(":
                stack.append("(")
            else:
                if not stack: # no opening present
                    c += 1
                    stack.append("(")
                
                if i+1 < len(s) and s[i+1] == ")": 
                    # it means it is a closing bracket
                    if stack and '(' == stack[-1]:  # match found
                        stack.pop()
                        i += 1
                        
                
                else:
                    # we reached end of s or next bracket is not )
                    c += 1
                    stack.pop()
            i += 1
        return len(stack)*2 + c      
        