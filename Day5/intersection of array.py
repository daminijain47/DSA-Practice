# Intersection of two arrays:
# q:Find the intersection of two arrays:
# common elements in the second array
# sample input: [1,2,2,1] and [2,2]
# output: [2]

arr1=[1,2,2,1]
arr2=[2,2]

arr3=[]

for i in range(len(arr1)):

    if arr1[i] in arr2:

        if arr1[i] not in arr3:
            arr3.append(arr1[i])

print(arr3)