# stock span problem
# example1: 
# input: N=7 
# price[]=[100, 80,60,70,60,75,85]
# output:: 1 1 1 8 1 8 8 
# explanation: 
# traversing the given input span for 100 will be 1,
#     80 is smaller than 100 so the span is 1,
# 60 is smaller tham 80 so the span is 1,
# 70 is greater than 60  so the span is 2,
# 60 is smaller then 70 so the span is 1,
# 75 is greater then 60 so the span is 2,
# 85 is greater then 75 so the span is 1,
# hence the output will be 1 1 1 2 1 2 2 



import sys

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()

    def peek(self):
        if len(self.stack) == 0:
            return None
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0


price = [100, 80, 60, 70, 60, 75, 85]

n = len(price)

span = [0] * n

s = Stack()

s.push(0)
span[0] = 1

for i in range(1, n):

    while (not s.isEmpty()) and price[s.peek()] <= price[i]:
        s.pop()

    if s.isEmpty():
        span[i] = i + 1
    else:
        span[i] = i - s.peek()

    s.push(i)

print("Stock Span:")

for i in range(n):
    print(span[i], end=" ")