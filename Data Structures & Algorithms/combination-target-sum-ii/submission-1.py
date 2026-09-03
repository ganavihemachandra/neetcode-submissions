class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        curr = [] # current combination
        candidates.sort()

        def dfs(i, total):
            if total == target:
                res.append(curr.copy())
                return
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                if total + candidates[j] > target:
                    break
                
                curr.append(candidates[j]) # include candidates[j]
                dfs(j+1, candidates[j] + total)
                curr.pop()
        dfs(0, 0)
        return res