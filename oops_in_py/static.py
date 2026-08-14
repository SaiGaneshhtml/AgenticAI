#@staticmethod
#static

class Coffeecup:

    @staticmethod
    def cup(iteam):
        return [ganesh.strip() for ganesh in iteam.split(",")]

raw ='  water ,suger  , milk'


# obj = Coffeecup()
# bee = obj.cup(raw)
# with out obj we use static 
bee = Coffeecup.cup(raw)
print(bee)