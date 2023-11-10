class Solution:
    def addDigits(self, num: int) -> int:
        l=[]
        while len(str(num))>1:
            l=[int(i) for i in str(num)]
            num=int(sum(l))
        return num
