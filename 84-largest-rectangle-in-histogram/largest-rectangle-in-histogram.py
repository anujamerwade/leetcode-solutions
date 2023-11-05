class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        maxArea = 0
        stack = []

        # first index
        stack = [0]

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                maxArea = self.getMaxArea(stack, heights, maxArea, i)
            stack.append(i)

        i = len(heights)
        while(stack):
            maxArea = self.getMaxArea(stack, heights, maxArea, i)


        return maxArea
    
    def getMaxArea(self,stack, heights, maxArea, i):
        area = 0
        popped = stack.pop()
        if not stack:
            area = heights[popped]*i
        else:
            area = heights[popped]*(i-1-stack[-1])
        return max(area, maxArea)
        