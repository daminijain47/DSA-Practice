class Parent:
    def __init__(self):
        self.speed=100
        print("Cash, Gold")

    def bike(self):
        print("Splender+ ",self.speed)

class Child(Parent):
    def __init__(self):
        self.speed=150
    def bike(self):
        print("HB",self.speed)
    

obj=Child()
obj.bike()