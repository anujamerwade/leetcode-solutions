class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        start = 0
        maxLength = 0

        if len(s) < 2:
            return len(s)
        for end in range(len(s)):
            if s[end] not in charSet:
                charSet.add(s[end])
                maxLength = max(maxLength, end-start + 1)
            else:
                while s[end] in charSet:
                    charSet.remove(s[start])
                    start += 1
                charSet.add(s[end])
        return maxLength