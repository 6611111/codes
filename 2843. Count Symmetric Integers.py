class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        c=0
        for i in range(low,high+1):
            s=str(i)
            n=len(s)
            if(n%2)!=0:
                continue
            f,se= s[:len(s)//2],s[len(s)//2:]
            l=[int(j) for j in f]
            m=[int(j) for j in se]
            if(sum(l)==sum(m)):
                c+=1
        return c
            
