s="the quick brown fox jumps over the lazy dog"

s=s.lower()

flag=True

for ch in "abcdefghijklmnopqrstuvwxyz":

    if ch not in s:
        flag=False
        break

if flag==True:
    print("Pangram")

else:
    print("Not Pangram")