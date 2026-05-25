#how to access data from the dict
d={}
d[100]="Aastha"
d[200]="Anisha"
d[300]="Kirty"
print(d)


rec={}
n=int(input("Enter number of studnets: "))
for i in range(n):
    name=input("Enter name: ")
    per=float(input("Enter percentage: "))
    rec[name]=per


print(rec)
for x in rec:
    print(x)
#output 
# aastha
# rushi

print(rec)
for x in rec:
    print(x,"\t",rec[x])

# output
# aastha   88.0
# anisha   99.0


