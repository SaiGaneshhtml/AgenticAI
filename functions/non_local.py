
def drink_type ():
    coffee_type = 'black coffee'

    def no_coffee():
        nonlocal coffee_type
        coffee_type = 'green_tea'
    no_coffee()
    print(f"here modifed with non local {coffee_type}")

drink_type()
# we use non locla for with in the 
# fun to modofy just above the vat not ablicable above the def fun 