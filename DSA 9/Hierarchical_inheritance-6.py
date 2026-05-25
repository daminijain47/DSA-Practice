class A:
    def showA(self):
        print("I am in class A")
class B(A):
    def showB(self):
        print("I am in class B")
class C(A):
    def showC(self):
        print("I am in class C")
class D(A):
    def showD(self):
        print("I am in class D")

if __name__=='__main__':
    obj1=B()
    obj1.showA()
    obj1.showB()

    obj2=C()
    obj2.showA()
    obj2.showC()

    obj3=D()
    obj3.showA()
    obj3.showD()

