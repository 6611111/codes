class Solution:
    def sortVowels(self, s: str) -> str:
       v=[]
       t=[]
       for i in s:
           if i.lower() in "aeiou":
               v.append(i)
       v.sort(reverse=True)
       for i in s:
           if i.lower() in "aeiou":
               t.append(v.pop())
           else:
                t.append(i)
       return "".join(t)
