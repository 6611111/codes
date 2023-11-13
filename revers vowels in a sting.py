class Solution:
    def reverseVowels(self, s: str) -> str:
       v=[]
       t=[]
       for i in s:
           if i.lower() in "aeiou":
               v.append(i)
       reversed(v)
       for i in s:
           if i.lower() in "aeiou":
               t.append(v.pop())
           else:
                t.append(i)
       return "".join(t)
