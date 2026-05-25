import sys
class GetNode:
    def __init__(self):
        self.left=None
        self.data=None
        self.right=None


class Linkedlist:
    def __init__(self):
        self.head=None

    def append(self):
        data=int(input("Enter data: "))
        newNode=GetNode()
        newNode.data=data
        if self.head is None:
            self.head=newNode
        else:
            ptr=self.head
            while ptr.right!=None:
                ptr=ptr.right
            ptr.right=newNode
            newNode.left=ptr
            

    def traverse(self):
        if self.head is None:
            print("list not present")
        else: 
            ptr=self.head
            while ptr!=None:
                print(ptr.data," <-> ", end="")
                ptr=ptr.right   
            print("None")
    
    def addAtBegin(self):
        data=int(input("Enter data: "))
        newNode=GetNode()
        newNode.data=data
        if self.head is None:
            self.head=newNode
        else:
            ptr=self.head
            newNode.right=ptr
            ptr.left=newNode
            self.head=newNode

    def addAtBetween(self):
        data=int(input("Enter data: "))
        key=int(input("Enter data after insertion: "))
        newNode=GetNode()
        newNode.data=data
        if self.head==None:
            self.head=newNode
        else:
            ptr=self.head
            
            while ptr !=None:
                if key==ptr.data:
                    break;
                else:
                    ptr=ptr.right
            if ptr==None:
                print("Key not found")
            else:
                newNode.right = ptr.right
                newNode.left = ptr
                if ptr.right != None:
                    ptr.right.left = newNode
                ptr.right = newNode
                print(data, " is added")



if __name__ == '__main__':
        obj = Linkedlist()

        while True:
            print("1. Append")
            print("2. Traverse")
            print("3. addAtBegin")
            print("4, addAtBetween")
            print("0. Exit")
            n=int(input("Select any choice: "))
            if n==1:
                obj.append()
            elif n==2:
                obj.traverse()
            elif n==3:
                obj.addAtBegin()
            elif n==4:
                obj.addAtBetween()
            elif n==0:
                sys.exit(0)
        