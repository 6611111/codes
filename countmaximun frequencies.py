class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            d[i]=nums.count(i)
        maxf=0
        for k,v in d.items():
            maxf=max(maxf,v)
        ans=0
        for k,v in d.items():
            if(maxf==v):
                ans+=v
        return ans
