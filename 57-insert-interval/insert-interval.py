class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        i = 0
        n = len(intervals)

        start = newInterval[0]
        end = newInterval[1]

        while i < n and intervals[i][1] < start:
            # out of this interval
            ans.append(intervals[i])
            i += 1
                 
        while i < n and end >= intervals[i][0]:
            # start is out of this interval
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1
        ans.append([start, end])

        while i < n:
            # start lies in this range
            ans.append(intervals[i])
            i += 1

        return ans
            