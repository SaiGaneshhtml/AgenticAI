# here we leran about attribut shadowing 

class Coffee():
    temp='hot'
    type='filter'


black = Coffee()
black.type = 'black'
print(black.type)

del black.type
print(black.type)# here there  type black is del now this will show filter this what we call 
# attributr shadowing here fall back will shown 

cup = Coffee()

cup.size = 'big'

print(cup.size)

del cup.size 

print(cup.size)#AttributeError: 'Coffee' object has no attribute 'size'
#here we declare  deletd no fall back so show error 
