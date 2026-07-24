# dictionary 
# we use dictionary to store data in key value pair insted index num we use name 
chai_water=dict(name="ginger chai", price=2.50)
print(f"the chai water is {chai_water}")
#name="ginger chai", price=2.50
tea_water=dict()
print(f"the tea water is {tea_water}")
#empty 
#buut we can add like this 
tea_water["name"]="masala tea"
tea_water["price"]=3.50
print(f"the tea water is {tea_water}")
print(f"the name of tea water is {tea_water['name']}")#masala tea
del tea_water["price"]
print(f"the tea water is {tea_water}")#price will remove

#with list 

chai_water=dict(name="ginger chai", price=2.50)
print(f"the chai water key is {chai_water.keys()}")
print(f"the chai water values are {chai_water.values()}")
print(f"the chai water items are {chai_water.items()}")

#update
coffee_water=dict(name="coffee water", price=66.50)
chai_water.update(coffee_water)
coffee_water.update(chai_water)# here we are updating the value of coffee water with chai water
print(f"the chai water is {chai_water}")#name will update to coffee water
print(f"the coffee water is {coffee_water}")#name will update to ginger chai

#safe way to get the value of key is using get method
#if the given optiomn naot avli it will not creash with help of get()not found will retun 
suger_water=chai_water.get("suger","not found try again")
print(f"the suger water is {suger_water}")#not found