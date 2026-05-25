#program to reverse internal content of each word 

s="Learning Python is very difficult from Ashish Sir"
ls=s.split()
print("".join(reversed(s)))


s = "Learning Python is very difficult from Ashish Sir"
ls = s.split()
for i in ls:
    print(i[::-1], end=" ")


   # blank variable fir ans = ans +