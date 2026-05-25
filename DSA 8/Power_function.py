def power(x, y):
    if y == 0:
        return 1
    elif y==0:
        return 1 
    elif y ==1:
        return x
    elif x==1:
        return 1
    else:
        return x * power(x, y-1)


# Example
print(power(2, 4))
