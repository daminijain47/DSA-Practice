import sys
class GetNode:
    def __init__(self):
        self.data=None
        self.next=None


class Linkedlist:
    def __init__(self):
        self.head=None

    def append(self):
        data=int(input("Enter data: "))
        newNode=GetNode()
        newNode.data=data
        if self.head==None:
            self.head=newNode
        else:
            ptr=self.head
            while ptr.next!=None:
                ptr=ptr.next
            ptr.next=newNode
            print(data," is added")


    def traverse(self):
        if self.head==None:
            print("Linked list not present")
        else:
            ptr=self.head
            while ptr!=None:
                print(ptr.data, " -> ", end="")
                ptr=ptr.next
            print("None")
    
    def addAtbegin(self):
        data=int(input("Enter data: "))
        newNode=GetNode()
        newNode.data=data
        if self.head==None:
            self.head=newNode
        else:
            ptr=self.head
            newNode.next=ptr
            self.head=newNode
        print(data, "is added at beginning")

    def addAtBetween(self):
        data=int(input("Enter data: "))
        key=int(input("Enter data after insertion: ")) #data kiske baad enter krna hai 
        newNode=GetNode()
        newNode.data=data
        if self.head==None:
            self.head=newNode
        else:
            ptr=self.head
            ptr1=ptr
            while ptr.next!=None:
                if key==ptr.data:
                    break;
                else:
                    ptr=ptr.next
            if ptr==None:
                print("Key not found")
            else:
                ptr1=ptr.next
                ptr.next=newNode
                newNode.next=ptr1
                print(data, " is added") 

    def deleteAtBegin(self):
        if self.head==None:
            print("list not present")
        else: 
            ptr=self.head
            ptr1=ptr.next
            ptr.next=None             
            head=ptr1
            print(ptr.data, "is deleted.")

    def deleteAtEnd(self):
        if self.head==None:
            print("list not present")
        else:
            ptr=self.head
            while ptr.next!=None:
                ptr1=ptr
                ptr=ptr.next
            ptr1.next=None
            print(ptr.data, "is delete from end.")

if __name__ == '__main__':
        obj = Linkedlist()

        while True:
            print("1. Append")
            print("2. Traverse")
            print("3. Add at begin")
            print("4. Add at Between")
            print("5. deleteAtBegin")
            print("6. deleteAtEnd")
            print("0. Exit")
            n=int(input("Select any choice: "))
            if n==1:
                obj.append()
            elif n==2:
                obj.traverse()
            elif n==3:
                obj.addAtbegin()
            elif n==4:
                obj.addAtBetween()
            elif n==5:
                obj.deleteAtBegin()
            elif n==6:
                obj.deleteAtEnd()
            elif n==0:
                sys.exit(0)
        