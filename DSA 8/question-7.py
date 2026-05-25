from itertools import permutations

a, b = map(int, input().split())

digits = str(a)

ans = []

# generate all permutations
for i in permutations(digits):

    num = int(''.join(i))

    # check number greater than b
    if num > b:
        ans.append(num)

# output
if len(ans) == 0:
    print(-1)
else:
    print(min(ans))