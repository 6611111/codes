class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        ans=[]
        i=0
        j=i+2
        while(i<n and j<n):
            o=[]
            for p in range(i,j+1):
                o.append(nums[p])
            c=0
            for e in range(0,2):
                if(abs(o[e]-o[e+1])<=k):
                    c+=1
            if(c==2):
                ans.append(o)
            else:
                ans.append([])
            i=j+1
            j=i+2
        return ans
