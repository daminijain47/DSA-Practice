# Rearrange postive and negative numbers:
# q: given an array containing both positive and negative number, rearrange them in an alternating fashion 
# logic: separate positive and negative numbers, then merge them alternately
# input: [-1,2,-3,4,5,-6]
# output: [-1,2,-3,4,-6,5]
 
# Separate negative and positive numbers

arr=[10,-5,20,-8,-1,7,15,-3]

negative=[]
positive=[]

for i in range(len(arr)):

    if arr[i] < 0:
        negative.append(arr[i])

    else:
        positive.append(arr[i])

print("Negative Array:",negative)
print("Positive Array:",positive)
