#sum of even and odd number 

n=int(input("Enter the size: ")) #
print("Enter the list element: ")
arr=[] #empty list 
even=0
odd=0
e1=0
o1=0
total=0 
for i in range(n):
    ele=int(input("Enter the element: "))
    arr.append(ele)

for j in range(len(arr)):
    total = total + arr[j]

    if i%2 ==0:
        even=even +i
        e1=e1+1
    else: 
        odd=odd + i
        o1=o1+1

print("Sum of elements: ", sum)
print("sum of even: ", even)
print("sum of odd: ", odd)
print("Count of even numbers: ", e1)
print("Count of odd numbers: ", o1)
#count e1 =0
#01==0 

# for j in range(len(arr)): #sir logic
#     if arr[i]%2 ==0:
#         even=even +arr[i]
#         e1=e1+1
#     else: 
#         odd=odd + arr[i]
#         o1=o1+1
