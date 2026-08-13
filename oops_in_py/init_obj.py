# constru  

class Chaicup:

    def __init__(self,type_,price):
        self.type_ = type_
        self.price = price

    def detailes(self):
        return f"coffee : {self.type_} & price = {self.price}rs"

order =Chaicup('black',300)
print(order.detailes())

order_2 =Chaicup('filter',398)
print(order_2.detailes())

        