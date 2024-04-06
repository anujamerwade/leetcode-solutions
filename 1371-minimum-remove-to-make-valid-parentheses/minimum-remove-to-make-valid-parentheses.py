class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        remove_indices = set()

        # Iterate through the string to find unmatched parentheses
        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            elif char == ")":
                if stack:
                    stack.pop()
                else:
                    remove_indices.add(i)

        # Mark remaining unmatched opening parentheses
        remove_indices.update(stack)

        # Construct the result string without the marked indices
        result = []
        for i, char in enumerate(s):
            if i not in remove_indices:
                result.append(char)

        return ''.join(result)
