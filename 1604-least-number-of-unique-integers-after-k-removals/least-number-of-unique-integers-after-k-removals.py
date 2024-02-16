class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = dict()

        for num in arr:
            freq[num] = 1 + freq.get(num, 0)
        
        sorted_freq = sorted(freq.values())

        res = 0
        idx = 0
        while k > 0 and idx < len(sorted_freq):
            if sorted_freq[idx] >= k:
                sorted_freq[idx] -= k
                k = 0
            else:
                balance = k - sorted_freq[idx]
                sorted_freq[idx] = 0
                k = balance
            idx += 1

        for num in sorted_freq:
            if num != 0:
                res += 1
        return res