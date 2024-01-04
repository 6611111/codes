class Solution:
    def minOperations(self, nums: List[int]) -> int:
        from collections import Counter
        mp=Counter(nums)
        res=0
        for i in mp.values():
            if i==1:
                return -1
            if(i%3==1):
                res+=(i//3)-1
                res+=2
            else:
                res+=i//3
                res+=(i%3)//2
        return res
            
