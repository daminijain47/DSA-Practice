import sys

class Queue:
    def __init__(self):
        self.queue=[]
        self.rear=-1
        self.front=0
        self.CAPACITY=5

    def isFull(self):
        if self.rear==self.CAPACITY-1:
            return True
        else:
            return False

    def insert(self,ele):
        if self.isFull():
            print("queue is full")
        else:
            self.rear=self.rear+1
            self.queue.append(ele)
            print(ele,"is inserted")
            
    def traverse(self):
        if self.isEmpty():
            print("queue is empty")
        else:
            for i in range(self.rear+1):
                print(self.queue[i])

    def isEmpty(self):
        if self.rear==-1:
            return True
        else:
            return False

    def delete(self):
        if self.isEmpty():
            print("queue is empty")
        else:
            ele=self.queue[self.front]

            for i in range(1,self.rear+1):
                self.queue[i-1]=self.queue[i]

            self.rear-=1
            return ele
    
    def peek(self):
        if self.isEmpty():
            print("queue is empty")
        else:
            print(self.queue[self.front])


class Stacks:
    def __init__(self):
        self.stack=[]
        self.top=-1
        self.CAPACITY=5

    def isFull(self):
        if self.top==self.CAPACITY-1:
            return True
        else:
            return False
        
    def push(self,ele):
        if self.isFull():
            print("stack is full")
        else: 
            self.top=self.top+1
            self.stack.append(ele)
            print(ele, "is pushed")

    def isEmpty(self):
        if self.top==-1:
            return True
        else:
            return False
        
    def pop(self):

        if self.isEmpty():
            print("Stack is Empty")
        else:
            ele=self.stack[self.top]
            self.stack.pop()
            self.top=self.top-1
            print(ele,"is popped")
            return ele
        
    def traverse(self):
        for i in range(self.top,-1,-1):
            print(self.stack[i])

    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
        else: 
            print(self.stack[self.top])


if __name__ == '__main__':

    obj1=Queue()
    obj2=Stacks()
    
    for i in range(obj1.CAPACITY):
        ele=int(input("Enter element: "))
        obj1.insert(ele)

    print("Original Queue")
    obj1.traverse()

    for i in range(obj1.CAPACITY):
        ele=obj1.delete()
        obj2.push(ele)

    print("Stack Elements")
    obj2.traverse()

    for i in range(obj2.CAPACITY):
        ele=obj2.pop()
        obj1.insert(ele)

    print("Reverse Queue")
    obj1.traverse()

    