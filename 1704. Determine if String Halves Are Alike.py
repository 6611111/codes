class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n=len(s)//2
        a=s[:n]
        b=s[n:]
        v1=0
        v2=0
        for i in a:
            if i in "AEIOUaeiou":
                v1+=1
        for i in b:
            if i in "AEIOUaeiou":
                v2+=1
        if(v1==v2):
            return True
        else:
            return False
