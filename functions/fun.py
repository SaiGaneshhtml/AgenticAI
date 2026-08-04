#here we learn param, argu,kwargs

#1st parameter

# chai = 'plaine chai'

# def chai_maker(order):
#     print(f"here we concat Making {order}")


# chai_maker(chai)
# print(f"here we print chai orginal don't change: {chai}")

#her now we use mutabl like list 

# chai_maker =['3','66','55']
# print(f"here we print chai orginal: {chai_maker}")

# def wow_maker(cup):
#     cup[2]=100

# wow_maker(chai_maker)
# print(f"here wow_ maker changed the list: {chai_maker}")

# the above is the parameter 

# here we learn about the args and kwargs

coffee= ['coffee','suger', 'water']

def coffee_maker(coffee, suger, water):# here we pass the args
    print(coffee, suger, water)

coffee_maker('yes','no','maybe')# position here we pass the args
coffee_maker(coffee ="no",suger="yes",water="maybe")# here we pass the keyword args

# now kwargu

def specal_coffee_maker(*args, **kwargs):
    print('args:', args)
    print('kwargs:', kwargs)
 #here we kwargus
specal_coffee_maker('coffee','suger',sugar='yes',water='no')