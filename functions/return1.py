# here we lean how add the 

def add_value (price,tax):
    return price * (100 + tax  )/100

orders=[130930,47234892389,2598975324989, 123]

#loop

for price in orders:
    finally_amont = add_value(price ,28.54)
    print(f"original price{price} , with tax{finally_amont}")