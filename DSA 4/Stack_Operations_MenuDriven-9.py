import sys

class Stacks:
   def __init__(self):
    self.stack = []
    self.top = -1
    self.CAPACITY = 5

   def isfull(self):
    if self.top == self.CAPACITY - 1:
      return True
    else:
      return False

   def push(self, ele):
    if self.isfull():
      print("stack is full")
    else:
      self.top = self.top + 1
      self.stack.append(ele)
      print(ele, "is pushed")

   def is_empty(self):
    if self.top == -1:
      return True
    else:
      return False

   def pop(self):
    if self.is_empty():
      print("stack is empty")
      return None # Indicate that pop failed
    else:
      ele = self.stack.pop()
      self.top = self.top - 1
      print(ele, "is popped")
      return ele

   def peek(self):
    if self.is_empty():
      print("stack is empty")
      return None
    else:
      print("Top element is:", self.stack[self.top])
      return self.stack[self.top]

   def traverse(self):
    if self.is_empty():
        print("Stack is empty.")
        return
    print("Stack elements:")
    for i in range(self.top, -1, -1):
        print(self.stack[i])


if __name__ == "__main__":
   obj = Stacks()
   while True:
    print('\n1.push')
    print('2.pop')
    print('3.peek')
    print('4.traverse')
    print('0.exit')
    try:
        ch = int(input("select any choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if ch == 1:
      try:
        ele = int(input('enter data: '))
        obj.push(ele)
      except ValueError:
        print("Invalid input. Please enter a number.")
    elif ch == 2:
      obj.pop()
    elif ch == 3:
      obj.peek()
    elif ch == 4:
      obj.traverse()
    elif ch == 0:
      sys.exit(0)
    else:
      print("invalid choice")



# 1.push
# 2.pop
# 3.peek
# 4.traverse
# 0.exit
# select any choice: 25
# invalid choice

# 1.push
# 2.pop
# 3.peek
# 4.traverse
# 0.exit
# select any choice: 26
# invalid choice

# 1.push
# 2.pop
# 3.peek
# 4.traverse
# 0.exit
# select any choice: 07
# invalid choice

# 1.push
# 2.pop
# 3.peek
# 4.traverse
# 0.exit
# select any choice: 09
# invalid choice

# 1.push
# 2.pop
# 3.peek
# 4.traverse
# 0.exit
# select any choice: 02
# stack is empty

# 1.push
# 2.pop
# 3.peek
# 4.traverse
# 0.exit
# select any choice: 03
# stack is empty

# 1.push
# 2.pop
# 3.peek
# 4.traverse
# 0.exit
# select any choice: 29
# invalid choice

# 1.push
# 2.pop
# 3.peek
# 4.traverse
# 0.exit