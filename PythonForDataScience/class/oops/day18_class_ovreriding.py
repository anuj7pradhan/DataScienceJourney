class A:
    def show(self):
        print("This is parent class")

class B(A):
    def show(self):
        print("This is child class")
        super().show()      # parent class ko method lai pani call garne

ob = B()
ob.show()
