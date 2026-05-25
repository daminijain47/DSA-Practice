# check for anagrams
# q: write a program to check if two string are anagrams of each other
# logic: check if the character counts in both strings are the same 
# input: "listen" and "silent"
# output: it is anagrams

s1=input("enter first string: ")
s2=input("enter second string: ")

if len(s1)==len(s2):

    flag=True

    for ch in s1:

        if s1.count(ch)!=s2.count(ch):
            flag=False
            break

    if flag==True:
        print("it is anagrams")

    else:
        print("it is not anagrams")

else:
    print("it is not anagrams")