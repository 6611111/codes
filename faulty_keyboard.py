class Solution:
    def finalString(self, s: str) -> str:
        res=""
        for k in s:
            if(k!='i'):
                res+=k
            if(k=='i'):
                res=res[::-1]
        return res
