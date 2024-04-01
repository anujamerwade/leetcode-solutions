class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lst = s.split()
        print(lst)

        return len(lst[-1])