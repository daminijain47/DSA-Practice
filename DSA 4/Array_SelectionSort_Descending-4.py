def selectionsort(arr):
  min=0
  loc=0
  for i in range(len(arr)-1):
    min=arr[i]
    loc=i
    for j in range(i+1,len(arr)):
       if arr[j]>min:
        min=arr[j]
        loc=j
        arr[i],arr[j]=arr[j],arr[i]
if __name__ == '__main__':
    arr=[6,23,26,2,1,5,4]
    selectionsort(arr)
    print(*arr)

