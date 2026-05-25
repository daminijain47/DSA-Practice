import re
str=input("Enter any string: ")
m=re.match(str, "abc@xyz_pqr*")
if m!=None:
    print("Yes matching is avaiable at beg")
    print('start index: ', m.start(),'. end index: ', m.end())
else:
    print("Matching is not avaiable at beg")