class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        s=0
        c=0
        for i in nums:
            s+=i
            if(s==0):
                c+=1
        if(c!=0):
            return c
        return 0
