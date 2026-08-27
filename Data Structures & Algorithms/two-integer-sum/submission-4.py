class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        for i in range(len(nums)):
            second = target - nums[i]
            if second in numMap:
                return [numMap[second], i]
            numMap[nums[i]] = i
        