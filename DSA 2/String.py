s="Learning Python is very easy from Ashish Sir"
print(s.find("Python")) #9
print(s.find("Java")) #-1
print(s.find("r")) #3
print(s.rfind("r"))  #43 it satrts it search each from right but give index number of exact place 


# output:
# 9
# -1
# 3
# 43

#----------------------------------------------------------

s="abcabcabcbabcabcabcdda"
print(s.count('a'))
print(s.count('ab'))
print(s.count('a',3,10))

# output:
# 7
# 6
# 2
#---------------------------------