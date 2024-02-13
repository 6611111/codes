class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        n=len(nums2)
        for i in nums1:
            ind=nums2.index(i)
            for j in range(ind+1,n):
                if(nums2[ind]<nums2[j]):
                    ans.append(nums2[j])
                    break
            else:
                ans.append(-1)
        return ans
