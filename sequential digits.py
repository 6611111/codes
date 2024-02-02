class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s="123456789"
        n=len(s)
        ans=[]
        for i in range(n):
            for j in range(i+1,n+1):
                curr=int(s[i:j])
                if(low<=curr<=high):
                    ans.append(curr)
            ans.sort()
        return ans



sequencial digits.py
