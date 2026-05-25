def linaer_serach(n,arr,target):

    flag=False

    for i in range(n):

        if target!=arr[i]:
            pass

        else:
            flag=True
            loc=i

    if flag==True:
        print("Search is successful and present at",loc)

    else:
        print("Search is unsuccessful")


if __name__=='__main__':

    n=int(input("enter the size of list:"))

    arr=[]

    for i in range(n):
        arr.append(int(input("enter the element:")))

    target=int(input("Enter no which is to be search:"))

    linaer_serach(n,arr,target) 