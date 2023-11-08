class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        res=""
        for i in words:
            a=i[0]
            res+=a
        if(res==s):
            return True
        else:
            return False
