class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sn=sorted(nums)
        l=[]
        for i in nums:
            l.append(sn.index(i))
        return l
