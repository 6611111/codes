s=input()
res=""
for i in range(len(s)):
    c=0
    for j in range(i+1,len(s)):
        if s[i]==s[j]:
            c+=1
    res=res+s[i]+str(c)
print(res)
