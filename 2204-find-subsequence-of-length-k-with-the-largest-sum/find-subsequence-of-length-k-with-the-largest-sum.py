class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        heap = []
        largest_elements = []
        for i in nums:
            heapq.heappush(heap, -i)
            
        heapq.heapify(heap)
        
        for i in range(k):
            largest_elements.append(-1*heapq.heappop(heap))
            
        elements_counter = {}
        for num in largest_elements:
            elements_counter[num] = 1 + elements_counter.get(num, 0)
        
        ans = []
        
        for num in nums:
            if num in elements_counter and elements_counter[num] > 0:
                ans.append(num)
                elements_counter[num] -= 1
                if len(ans) == k:
                    break
        
        return ans
            