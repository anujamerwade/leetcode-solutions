class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map = dict()

        l = 0

        if len(s) != len(t):
            return False

        for l in range(len(s)):
            if s[l] not in map:
                if t[l] not in map.values():
                    map[s[l]] = t[l]
                else:
                    return False
            else:
                if map[s[l]] != t[l]:
                    return False
        return True
        