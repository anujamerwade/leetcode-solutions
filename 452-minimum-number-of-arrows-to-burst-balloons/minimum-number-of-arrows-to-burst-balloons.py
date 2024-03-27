class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()

        res = len(points)
        prevInterval = points[0]

        for i in range(1, len(points)):
            curr = points[i]

            if curr[0] <= prevInterval[1]:
                res -= 1
                prevInterval = [curr[0], min(curr[1], prevInterval[1])]
            else:
                prevInterval = curr
        return res
