class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d={}
        for i in s:
            d[i]=s.count(i)
        ans=""
        for i in order:
            if i in d.keys():
                for k,v in  d.items():
                    if(i==k):
                        ans+=i*v
        for i in s:
            if s.count(i)!=ans.count(i):
                ans+=i
        return ans
            
