# here we learn about refence and , self usinf 

class Cupcoffee:
    size=120#ml

    def user(self):
        return f'this size {self.size}'

cup = Cupcoffee()
#TYPE 1
print('type 1',cup.user())
#TYPE 2 
print('type 2',Cupcoffee.user(cup))