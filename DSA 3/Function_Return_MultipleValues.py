#function retur multiple values
def add(a,b):
  res1=a+b
  res2=a-b
  res3=a*b
  res4=a/b
  return res1,res2,res3,res4
if __name__ == '__main__':
     a=int(input("enter a:"))
     b=int(input("enter b:"))
     r1,r2,r3,r4=add(a,b)
     print("addition is",r1)
     print("subtraction is",r2)
     print("multiplication is",r3)
     print("division is",r4)


# enter a:25
# enter b:26
# addition is 51
# subtraction is -1
# multiplication is 650
# division is 0.9615384615384616