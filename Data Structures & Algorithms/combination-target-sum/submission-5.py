class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = [] # current combination
        nums.sort()

        def dfs(i, total):
            if total == target:
                res.append(curr.copy())
                return
            
            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    break
                
                curr.append(nums[j]) # include nums[j]
                dfs(j, total + nums[j])
                curr.pop() # exclude nums[j]
        dfs(0, 0)
        return res