#rotation an array to the right by a given number of steps
#sample input: [1,2,3,4,5] rotated by 2 steps 
#ecpected output : [4,5,1,2,3]
#  array rotation 
# rotation of array to the right by given steps

# arr=[1,2,3,4,5]

# Temp=2

# print("Input:",arr)

# for i in range(Temp):

#     last=arr[len(arr)-1]

#     for j in range(len(arr)-1,0,-1):
#         arr[j]=arr[j-1]

#     arr[0]=last

# print("Output:",arr)

arr=[1,2,3,4,5]
k=2
for i in range(k):
    temp=arr[-1]
    for i in range(len(arr)-1,0,-1):
        arr[i]=arr[i-1]
    arr[0]=temp

print(arr)