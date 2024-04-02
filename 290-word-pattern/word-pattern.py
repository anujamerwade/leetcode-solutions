class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map = dict()

        words = s.split()

        if len(pattern) != len(words):
            return False
        
        for l in range(len(pattern)):
            if pattern[l] not in map:
                if words[l] not in map.values():
                    map[pattern[l]] = words[l]
                else:
                    return False
            else:
                if map[pattern[l]] != words[l]:
                    return False
        return True