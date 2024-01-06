class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        a=0
        for i in arr1:
            c=0
            for j in arr2:
                diff=abs(i-j)
                if(diff>d):
                    c+=1
            if(len(arr2)==c):
                a+=1
        return a
