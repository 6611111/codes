class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        a=nums[0]
        b=nums[1]
        return (a-1)*(b-1)
