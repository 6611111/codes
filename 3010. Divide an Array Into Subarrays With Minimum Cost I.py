class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        n=len(nums)
        #i#f(n<=3):
         #   return sum(nums)
        s=nums[0]
        nums[1:n]=sorted(nums[1:n])
        s+=nums[1]+nums[2]
        return s
