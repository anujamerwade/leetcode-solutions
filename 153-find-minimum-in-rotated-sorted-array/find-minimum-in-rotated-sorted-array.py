class Solution:
    def findMin(self, nums: List[int]) -> int:

        pivot = self.findPivot(nums)

        if pivot == -1:
            return nums[0]  # nums is already sorted
        return pivot
        
    
    def findPivot(self, arr):
        s = 0
        e = len(arr) - 1
        

        while (s <= e):
            m = s + (e-s)//2
            if (m < e and arr[m+1] < arr[m]):
                return arr[m+1]
            elif (m > s and arr[m-1] > arr[m]):
                return arr[m]
            else:
                if arr[s] <= arr[m]:
                    s = m + 1
                else:
                    e = m - 1
        return -1