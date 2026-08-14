# method resolution order

class A:
    lable = "A"

class B(A):
    lable = "B"

class C(B):
    lable = "c"
    
# Rule in your words: child always comes first, 
# parent comes after — write it as (child, parent) never (parent, child).
# So (C,A) ✅, (C,B) ✅, (B,A) ✅ — all work because child is listed first.
# (A,C) ❌, (A,B) ❌, (B,C) ❌ — all fail because parent is listed
#  before its own child.


class D(C,A):# i will see B what ever 1st ele there it will excute 
    pass

cup = D()
print (cup.lable)
print(D.__mro__)