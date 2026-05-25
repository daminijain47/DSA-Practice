#decending  order
def bubblesort(arr):
  for i in range(len(arr)-1):
    for j in range(len (arr)-1-i):
      if arr[j] < arr[j+1]:
        arr[j],arr[j+1]=arr[j+1],arr[j]

if __name__ == '__main__':
  arr=[6,23,26,2,1,5,4]
  bubblesort(arr)
  print(*arr)

#   26 23 6 5 4 2 1