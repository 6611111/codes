class Solution:
    def maxSum(self, nums: List[int]) -> int:
        l=[]
        for i in range(len(nums)):
            a=str(nums[i])
            for j in range(i+1,len(nums)):
                b=str(nums[j])
                if(max(a)==max(b)):
                    s=int(a)+int(b)
                    l.append(s)
        if(len(l)==0):
            return -1
        else:
            return max(l)
