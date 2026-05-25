# Check for a valid palindrome string:
#     q: write  program to check if a given string is a valid palindromic string after ignoring non-alphanumeric characters and considering case
# logic: use loops to compare characters while ignoring non-alphanumeric characters
# input: "A man, a plan,  a canal: panama"
# output: Valid palindrome

s="A man, a plan,  a canal: panama"
str=""

for x in s:
    if x.isalpha():
        str=str+x
print(str)
str=str.lower()
print(str)
rev=str[::-1]
if rev==str:
    print("Valid palindrome")
else:
    print("Not palindrome")

