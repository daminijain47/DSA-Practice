for i in range(1,5):
    for j in range(1,5):
        print(i,end=" ")
    print()
# output:
# 1 1 1 1 
# 2 2 2 2 
# 3 3 3 3 
# 4 4 4 4
#-----------------------
for i in range(1,5):
    for j in range(1,5):
        print(j,end=" ")
    print()

# output
# 1 2 3 4 
# 1 2 3 4 
# 1 2 3 4 
# 1 2 3 4 
#-------------------------------
n=1
for i in range(1,5):
    for j in range(1,5):
        print(j,end="\t")
        n=n+1
    print()

# output:
# 1       2       3       4
# 1       2       3       4
# 1       2       3       4
# 1       2       3       4


n=65
for i in range(1,5):
    for j in range(1,5):
        print(n,end="\t")
        n=n+1
    print()

# output:
# 65      66      67      68
# 69      70      71      72
# 73      74      75      76
# 77      78      79      80

#--------------------------

n=65
for i in range(1,5):
    for j in range(1,5):
        print(chr(n),end="\t")
        n=n+1
    print()

# output:
# A       B       C       D
# E       F       G       H
# I       J       K       L
# M       N       O       P

#-----------------------------

for i in range(1,5):
    for j in range(1,i+1):
        print(i,end=" ")
    print()

# output:
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
#---------------------------

for i in range(4,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

# output:
# * * * * 
# * * * 
# * * 
# * 

#--------------------------------------

sp=0
for i in range(4,0,-1):
    for x in range(sp):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
    sp=sp+1

# output:
# * * * * 
#  * * * 
#   * * 
#    * 