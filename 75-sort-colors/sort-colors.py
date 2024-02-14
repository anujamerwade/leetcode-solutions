class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # dutch national flag algo
        """
        The problem was posed with three colors, here `0′, `1′ and `2′. The array is divided into four sections: 
        arr[1] to arr[low – 1]
        arr[low] to arr[mid – 1]
        arr[mid] to arr[high – 1]
        arr[high] to arr[n]
        If the ith element is 0 then swap the element to the low range.
        Similarly, if the element is 1 then keep it as it is.
        If the element is 2 then swap it with an element in high range.
        """
        lo = 0
        mid = 0
        hi = len(nums) - 1

        while mid <= hi:
            if nums[mid] == 0:
                nums[lo], nums[mid] = nums[mid], nums[lo]
                lo += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[hi], nums[mid] = nums[mid], nums[hi]
                hi -= 1
        return nums
