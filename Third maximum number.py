class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nl=list(set(nums))
        n=len(nl)
        nl.sort(reverse=True)
        if(n>=3):
            return nl[2]
        else:
            return nl[0]
