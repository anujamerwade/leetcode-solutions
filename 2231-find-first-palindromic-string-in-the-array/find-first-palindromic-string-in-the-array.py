class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        ans = ""
        for word in words:
            if word == word[::-1]:
                return word
        return ans

    #     l = 0
    #     r = len(word)-1
    #     while l <= r:
    #         if word[l] == word[r]:
    #             l += 1
    #             r -= 1
    #         else:
    #             break
    #     if l > r:
    #         # word is palindrome
    #         return word
    # return ans 
        