class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        hashmap = {}

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        
        val_list = list(hashmap.values())
        max_freq = max(val_list)

        ans = 0

        for n in val_list:
            if n == max_freq:
                ans += max_freq
        return ans
    # TC: O(n)
    # SC: O(n)