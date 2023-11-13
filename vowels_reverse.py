class Solution:
    def sortVowels(self, s: str) -> str:
       v=[]
       t=""
       for i in s:
           if i in "AEIOUaeiou":
               v.append(i)
       sorted(v)
       j=0
       for i in range(len(s)):
            while(j<len(v)):
                if s[i] in v:
                    t+=v[j]
                    j+=1
            else:
                t+=s[i]
       return t
