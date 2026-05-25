import re
str=input("Enter any string: ")
m=re.fullmatch(str, "abcabcabc")
if m!=None:
    print("Yes matching is avaiable at beg")
    #print('start index: ', m.start(),'. end index: ', m.end())
else:
    print("Matching is not avaiable at beg")


#question is asked what is match and fullmatch 