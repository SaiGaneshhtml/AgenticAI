# here we look into inher and composition 

class A:

    def __init__(self,type_):
        self.type = type_

    def Smalla(self):
        print(f"a {self.type}")

    def Add(self):
        print (f"i like {self.type} tea")

class B(A):

     pass

class D:
    bat = A

    def __init__(self):
        self.cat = self.bat('reguler')



ball_1 =B('masala')
B.Add(ball_1)

work =D()      # this IS your A object, already created, already has type='reguler'
work.cat.Add()  # call A's Add() method on it -> prints "i like reguler tea"
work.cat.Smalla()