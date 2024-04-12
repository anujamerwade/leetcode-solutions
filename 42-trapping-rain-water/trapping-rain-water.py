class Solution:
    def trap(self, height: List[int]) -> int:
        maxCap = 0
        n = len(height)
        e, s = n-1, 0
        maxLeft, maxRight = 0, 0

        while s <= e:
            if height[s] <= height[e]:
                if height[s] >= maxLeft:
                    maxLeft = height[s]
                else:
                    maxCap += maxLeft - height[s]
                s += 1
            else:
                if height[e] >= maxRight:
                    maxRight = height[e]
                else:
                    maxCap += maxRight - height[e]
                e -= 1
        return maxCap