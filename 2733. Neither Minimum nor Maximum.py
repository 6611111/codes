class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if(len(nums)==2):
            return -1
        ma=max(nums)
        mi=min(nums)
        for i in nums:
            if (i==ma or i==mi):
                continue
            else:
                return i
        return -1
