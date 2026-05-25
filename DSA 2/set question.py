#accept values from user and print it 

n=int(input("Enter the size: ")) #
print("Enter the list element: ")
arr=[] #empty list 
for i in range(n):
    ele=int(input("Enter the element: "))
    arr.append(ele)

for i in range(len(arr)):
    print(arr[i])  #print(arr[i],end=" ") to get output in one line   