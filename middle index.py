class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n=-1
        if(len(nums)==1):
            return 0
        for i in range(len(nums)):
            ls=0
            rs=0
            for k in range(i+1):
                ls+=nums[k]
            for j in range(i+2,len(nums)):
                rs+=nums[j]
            if(i==0 and nums[i]==0):
                return 0
            if(ls==rs):
                n=i+1
                break
        return n
