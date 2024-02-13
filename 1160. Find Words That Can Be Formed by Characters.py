class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        s=0
        for i in words:
            c=0
            for j in i:
                if j in chars and (i.count(j)<=chars.count(j)):
                    c+=1
                else:
                    break
            if(c==len(i)):
                s+=len(i) 
        return s                       
