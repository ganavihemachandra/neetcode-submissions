class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        # rob1, rob2, 1, 2, 3, 1

        for n in nums:
            curRob = max(rob1+n, rob2)
            rob1 = rob2
            rob2 = curRob
        return rob2