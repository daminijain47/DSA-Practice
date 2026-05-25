class A:
    def showA(self):
        print("I am in class A")
class B:
    def showB(self):
        print("I am in class B")
class C:
    def showC(self):
        print("I am in class C")
class D(A,B,C):
    def showD(self):
        print("I am in class D")

if __name__=='__main__':
    obj=D()
    obj.showA()
    obj.showB()
    obj.showC()
    obj.showD()


