#int  
tea_with = 10
coffee_with = 22

total_drinks = tea_with + coffee_with
print(f"Total drinks: {total_drinks}")


apples = 5
apples_with_red = 3
total_apples = apples - apples_with_red
print(f"Total apples: {total_apples}")

milke =19
galss=5
total_milk = milke * galss
print(f"Total milk: {total_milk}")

# // use this for round off
penut= 100
nut= 7
totalremaining_nuts = penut // nut
print(f"Total remaining nuts: {totalremaining_nuts}")

# / use for division
apple = 10
orange = 3  
total_fruits = apple / orange
print(f"Total fruits: {total_fruits}")

# % use for remainder
total_remaining_fruits = apple % orange 
print(f"Total remaining fruits: {total_remaining_fruits}")

#boolean we use True /False 

IS_Raining = True
print(f"Is it raining? {IS_Raining}")

#  TRUE = 1
#  FALSE = 0

IS_raining = 1
apple = 0
total_fruits = apple + IS_raining
print(f"Total fruits: {total_fruits}")
#here true is 1 so it will add 1 to apple and give total fruits as 11
#this type of boolean is used in conditional
#we call upcasting where boolen value is converted to integer value
#0, none are retuned as false and any other value is returned as true

print(f"Boolean value of 0: {bool(apple)}") #False
print(f"Boolean value of None: {bool(None)}") #False
print(f"Boolean value of 11: {bool(11)}") #True
print(f"Boolean value of 'sai': {bool('sai')}") #True