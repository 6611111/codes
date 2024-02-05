class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in s:
            c=s.count(i)
            if(c==1):
                return s.index(i)
                break
        return -1
