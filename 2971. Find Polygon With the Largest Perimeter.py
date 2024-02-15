class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort();
        for i in range(n-1,0,-1):
            s=0
            for j in range(0,i):
                s+=nums[j]
            if(s>nums[i]):
                return nums[i]+s
                break
        return -1
