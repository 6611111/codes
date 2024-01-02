class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        res=[]
        freq=[0]*(len(nums)+1)
        for i in nums:
            if(freq[i]>=len(res)):
                res.append([])
            res[freq[i]].append(i)
            freq[i]+=1
        return res
