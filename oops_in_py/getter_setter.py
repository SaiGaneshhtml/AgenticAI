# we can set vaule and err in 
#gettters and setters 

class Cup:

    def __init__(self,age):
        self.age = age
 # = the PROPERTY (has the gate/rules) — use this from OUTSIDE, and in __init__
# = the STORAGE (plain variable, no rules) — use this ONLY inside getter/setter body
    #getters
    @property
    def age(self):
        return self._age + 1
    #setters
    @age.setter
    def age(self,age):
        if 1<= age <=9:
            self._age=age
        else:
            raise ValueError('error')

bee = Cup(1)
print(bee.age)

bee_0= Cup(5)
print(bee_0.age)

bee_9 =Cup(66)
print(bee_9.age)