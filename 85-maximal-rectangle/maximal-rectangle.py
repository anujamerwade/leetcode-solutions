class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        r = len(matrix)
        c = len(matrix[0])

        currRow = [0]*c
        maxAreaFinal = self.largestRectangleArea(currRow)

        for i in range(r):
            for j in range(len(matrix[i])):
                if matrix[i][j] == str(1):
                    currRow[j] += 1
                else:
                    currRow[j] = 0
            currArea = self.largestRectangleArea(currRow)

            maxAreaFinal = max(currArea, maxAreaFinal)
        return maxAreaFinal

    def largestRectangleArea(self, heights):

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

# TC: O(r*c)
# SC: (n)