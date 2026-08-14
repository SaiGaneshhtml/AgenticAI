# here we learn about cls methode 
# we can't use multp construter with help cls we make it look like

class Coffee:
    def __init__(self,suger,power):
        self.suger=suger
        self.power=power

    @classmethod
    def from_dice (cls, order_data ):
        return cls(
    suger=order_data['suger'],
    power=order_data['power'],
    )
    
class Chai:
    @staticmethod
    def form_chai(size):   
        return size in ['L','M','S']

print(Chai.form_chai('M'))

order1 = Coffee.from_dice({"suger":"less" , "power" : "more"})
print(order1.__dict__)