#accept values from user and find sum of list

# n=int(input("Enter the size: ")) #
# print("Enter the list element: ")
# arr=[] #empty list 
# sum=0

# for i in range(n):
#     ele=int(input("Enter the element: "))
#     arr.append(ele)

# for j in range(n):
#     ele=int(input("Enter the element: "))
#     arr.append(ele)

# sum=sum+arr[i]+arr[j]
# print(sum)

n=int(input("Enter the size: ")) #
print("Enter the list element: ")
arr=[] #empty list 
sum=0

for i in range(n):
    ele=int(input("Enter the element: "))
    arr.append(ele)

for j in range(len(arr)):
    sum=sum+arr[i]

#CHECK
