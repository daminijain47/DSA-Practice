import re
x="[abc]" #print only abc
x="[^abc]" #leaving abc print other things
x="[a-z]" #print a-z small alphabeth
x="[0-9]" #print 0-9 number only digit \d se bhi aata hai
x="[^0-9]" 
x="[a-zA-Z0-9]" #print all of these 
x="[^a-zA-Z0-9]" # leaving this print other symbol 

matcher=re.finditer(x,"a7bD2@k2$D8z")
#print(matcher)
for match in matcher:
    print(match.start(),'...',match.group())