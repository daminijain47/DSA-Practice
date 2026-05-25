#Tokenization 
s="Learning Python is very difficult from Ashish Sir"
ls=s.split()
print(ls)
print(len(ls)) #8

# output:
# ['Learning', 'Python', 'is', 'very', 'difficult', 'from', 'Ashish', 'Sir']
# 8
#--------------------------

s="22-02-2022"
ls=s.split("-")
print(ls)

# output:
# ['22', '02', '2022']
#--------------------------------

s="www.ashish.com"
s="22-02-2022"
ls=s.split(".")
print(ls)

# output:
# ['22-02-2022']

s="Learning Python is very difficult from Ashish Sir"
ls=s.split()
print(" ".join(reversed(ls)))

# Sir Ashish from difficult very is Python Learning

