def insertionsort(arr):
  for i in range(len(arr),1):
    current=arr[i]
    loc=i
    while current<arr[loc-1] and loc>0:
        arr[loc]=arr[loc-1]
        loc=loc-1
        arr[loc]=current
if __name__ == '__main__':
    arr=[6,23,26,2,1,5,4]
    insertionsort(arr)
    print(*arr)