class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        l1=[]
        l2=[]
        for i in nums:
            if(i>0):
                l1.append(i)
            else:
                l2.append(i)
        nums=[sub[item] for item in range(len(l1))
                      for sub in [l1, l2]]
        return nums
