class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subSet = []
        nums.sort()

        def dfs(i):
            res.append(subSet.copy())

            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue
                
                subSet.append(nums[j])
                dfs(j+1)
                subSet.pop()
        dfs(0)
        return res