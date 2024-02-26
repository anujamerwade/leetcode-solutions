class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1
        
        val_list = list(freq.values())
        key_list = list(freq.keys())
        majorityEleCount = max(val_list)

        ans = val_list.index(majorityEleCount)
        return key_list[ans]
        