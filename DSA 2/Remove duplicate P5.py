s="ABCDABCDABCDABCDABCDE"
ls=s.split()
ans=""
for i in s:
    if i not in ans:
        ans=ans+i
print(ans)




