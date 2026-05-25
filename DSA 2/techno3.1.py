no=248316 #998001tech no
save=no
count=0
while no>0:
    no=no//10
    count=count+1

no=save

if count%2==0:
    mid=count//2   
    n1=no%10**mid
    n2=no//10**mid
    sum=n1+n2
    sum=sum**2 #sq=sum*sum

    if sum==no:
            print("Tech Number")
    else:
            print("Not Tech Number")

