class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        ht, wt = len(mat), len(mat[0])
        painted_row = [0 for _ in range(ht)]
        painted_col = [0 for _ in range(wt)]
        valuesToPosition = {}

        for i in range(ht):
            for j in range(wt):
                valuesToPosition[mat[i][j]] = (i, j)
        
        for i in range(len(arr)):
            paint_row, paint_col = valuesToPosition[arr[i]]
            painted_row[paint_row] += 1
            painted_col[paint_col] += 1
            if painted_col[paint_col] == ht or painted_row[paint_row] == wt:
                return i
        return -1