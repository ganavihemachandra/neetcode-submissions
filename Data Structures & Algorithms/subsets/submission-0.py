class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subSet = [] # current subSet

        def dfs(i):
            if i >= len(nums):
                res.append(subSet.copy())
                return
            
            # include
            subSet.append(nums[i])
            dfs(i+1)

            # don't include
            subSet.pop()
            dfs(i+1)
        dfs(0)
        return res