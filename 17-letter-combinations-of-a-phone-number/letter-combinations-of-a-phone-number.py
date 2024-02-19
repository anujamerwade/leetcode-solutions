class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        return self.helper("", digits)
    
    def helper(self, p, up):
        if up == "":
            return [p]
        
        digit = int(up[0])
        letters = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res = []

        for ch in letters[up[0]]:
            res.extend(self.helper(p + ch, up[1:]))
        return res
        