class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        candidates.sort()

        def backtrack(curr, pos, target):
            if target == 0:
                res.append(curr.copy())
                return
            if pos >= len(candidates) or target <= 0:
                return

            prev = -1
            for i in range(pos, len(candidates)):
                # do not want to repeat a cand
                if candidates[i] == prev:
                    continue
                
                curr.append(candidates[i])
                backtrack(curr, i + 1, target - candidates[i])
                # backtrack clean up
                curr.pop()
                prev = candidates[i]
        
        backtrack([], 0, target)

        
        return res