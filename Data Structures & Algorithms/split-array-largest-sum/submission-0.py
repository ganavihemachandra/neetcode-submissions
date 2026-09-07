class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(largest):
            subarray = 0
            curSum = 0
            for n in nums:
                curSum += n
                if curSum > largest:
                    subarray += 1
                    curSum = n
            return 1 + subarray <= k
        
        l, r = max(nums), sum(nums)
        while l <= r:
            mid = l + ((r-l)//2)
            if canSplit(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res