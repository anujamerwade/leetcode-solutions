class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        i = 0

        def dfs(i, curr, total):
            # combo found
            if total == target:
                res.append(curr.copy())
                # curr.copy() creates a shallow copy of the curr list. 
                # This ensures that any changes made to curr after appending it 
                # to res won't affect the combination stored in res. It's
                # important to use .copy() here to avoid appending a reference 
                # to the same list multiple times, which would lead to incorrect 
                # results.
                return
            
            # unable to find a combo
            if i >= len(candidates) or total > target:
                return
            
            curr.append(candidates[i])
            # include candidate
            dfs(i, curr, total+candidates[i])

            # backtrack and remove the added candidate
            curr.pop()
            dfs(i+1, curr, total)   # i + 1 because you add the next one
        dfs(0, [], 0)
        return res





# TC: 2^target
# SC: 