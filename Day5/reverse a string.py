# reverse a string without inbuild function and shortcut:
# q: Write a program to reverse a given string
# input: "hello"
# output: "olleh"

s="Hello"
rev=""
for i in s:
    rev=i +rev
print(rev)