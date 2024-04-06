class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        open = 0
        arr = list(s)

        # from left to right
        for i in range(len(arr)):
            if arr[i] == "(":
                open += 1
            elif arr[i] == ")":
                if open == 0:
                    arr[i] = "*"
                else:
                    open -= 1

        # from right to left if we encounter extra open braces
        for i in range(len(arr)-1, -1, -1):
            if open > 0 and arr[i] == "(":
                arr[i] = "*"
                open -= 1

        result = ''.join(c for c in arr if c != '*')

        return result