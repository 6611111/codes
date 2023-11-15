class Solution:
    def countDigits(self, num: int) -> int:
        l=[int(i) for i in str(num)]
        c=0
        for i in l:
            if(num%i==0):
                c+=1
        return c
