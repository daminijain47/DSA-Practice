import sys
class BST:
    def insert(self):
        pass
    def preorder(self):
        pass
    def postorder(self):
        pass
    def inorder(self):
        pass


if __name__ == '__main__':
    root=BST()
    while True:
        print("1. Insert")
        print("2. Preorder")
        print("3. Postorder")
        print("4. Inorder")
        print("0. Exit")
        n=int(input("Select any choice: "))
        if n==1:
            root.insert()
        elif n==2:
            root.preorder()
        elif n==3:
            root.postorder()
        elif n==4:
            root.inorder()
        elif n==0:
                root.exit(0)