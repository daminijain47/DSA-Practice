# Implementing Queue using Linked List

import sys

class GetNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    # Insert operation
    def insert(self, ele):

        newNode = GetNode(ele)

        # If queue is empty
        if self.front is None:
            self.front = self.rear = newNode

        else:
            self.rear.next = newNode
            self.rear = newNode

        print(ele, "inserted into queue")

    # Delete operation
    def delete(self):

        if self.front is None:
            print("Queue is empty")

        else:
            ele = self.front.data
            self.front = self.front.next

            # If queue becomes empty
            if self.front is None:
                self.rear = None

            print("Deleted element is:", ele)

    # Traverse operation
    def traverse(self):

        if self.front is None:
            print("Queue is empty")

        else:
            temp = self.front

            print("Queue elements are:")

            while temp is not None:
                print(temp.data, end=" ")
                temp = temp.next

            print()


# Main Program
if __name__ == '__main__':

    q = Queue()

    while True:

        print("\n1.Insert")
        print("2.Delete")
        print("3.Traverse")
        print("4.Exit")

        ch = int(input("Enter your choice: "))

        if ch == 1:

            ele = int(input("Enter element: "))
            q.insert(ele)

        elif ch == 2:

            q.delete()

        elif ch == 3:

            q.traverse()

        elif ch == 4:

            sys.exit()

        else:

            print("Invalid choice")