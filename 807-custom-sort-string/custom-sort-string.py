class Solution:
    def customSortString(self, order: str, s: str) -> str:

        ans = ""
        orderMap = {}
        sMap = {}

        # make orderMap as dict of indices
        for idx, ch in enumerate(order):
            orderMap[ch] = idx
        
        # make sMap as dict of freq
        for ch in s:
            sMap[ch] = 1 + sMap.get(ch, 0)
        
        for k, v in orderMap.items():
            if k in sMap:
                ans += k*sMap[k]

        for k, v in sMap.items():
            if k not in orderMap:
                ans += k*sMap[k]
        
        return ans


        