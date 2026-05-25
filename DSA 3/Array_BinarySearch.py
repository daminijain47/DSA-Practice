# def binary_serach(n,arr,target):
#   flag= False
#   low=0
#   high=n-1
#   while low<=high:
#     mid=(low+high)//2
#     if target==arr[mid]:
#         flag=True
#         loc=mid
#         break;
#     elif
#         target<arr[mid]:
#         high=mid-1
#     elif
#        target>arr[mid]:
#        low=mid+1

#  if __name__=='__main__':
#        n=int(input("enter the size of list:"))
#        arr=[]
#        for i in range(len(n)):
#            arr[i]= append (int(input("enter the element:")))
#      target=int(input("enter the target element:"))
#      linear_search(n,arr,target)

def binary_serach(n,arr,target):
    flag=False
    low=0
    high=n-1

    while low<=high:
        mid=(low+high)//2

        if target==arr[mid]:
            flag=True
            loc=mid
            break

        elif target<arr[mid]:
            high=mid-1

        elif target>arr[mid]:
            low=mid+1

    if flag==True:
        print("element found at location",loc)
    else:
        print("element not found")


if __name__=='__main__':

    n=int(input("enter the size of list:"))

    arr=[]

    for i in range(n):
        arr.append(int(input("enter the element:")))

    target=int(input("enter the target element:"))

    binary_serach(n,arr,target)