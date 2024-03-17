class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        c = 0
        ans = 0
        hm = {0: -1}  # Initialize the hash map with prefix sum 0 at index -1

        for i in range(len(nums)):
            c += 1 if nums[i] == 1 else -1

            if c in hm:
                # If the current prefix sum is seen before, update the answer
                ans = max(ans, i - hm[c])
            else:
                # Store the index of the first occurrence of the prefix sum
                hm[c] = i

        return ans