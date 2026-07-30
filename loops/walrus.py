#here we leran how to use walrus oper 
#this make thing easy like input and evaulvater in one line 

drinks = ['tea', 'coffee', 'water', 'juice']
print(f"choose the drinks :{drinks}")

while (drink := input(f"choose a drink : ").lower() ) not in drinks:
    print(f"sorry u r choosen dirnk not avali : {drink}")
    
else:
    print(f"here is u r choosen drink : {drink}")