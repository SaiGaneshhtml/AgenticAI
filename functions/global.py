# here global

coffee_type = 'black coffee'
def drink_type ():

    def no_coffee():
        global coffee_type
        coffee_type = 'green_tea'
    no_coffee()
    print(f"here modifed with non local {coffee_type}")

drink_type()

#same exp above the fun we can globale word to modify the data 
# just above the def fun we use local
#above the def fun we need use global
