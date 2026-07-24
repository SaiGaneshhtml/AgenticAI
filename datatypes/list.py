# mutable list implementation
# we can change the list in place.
chai_type=["masala","ginger","cardamom","clove"]
print(f"the chai type is {chai_type}")
chai_type.append("cinnamon")
#alway add last in the list
print(f"the chai type is {chai_type}")

####
chai_type=["tea"]
coffee_type=["coffee"]

coffee_type.extend(chai_type)
print(f"the coffee type is {coffee_type}")
# merge two list using extend method
# chai_type.extend(coffee_type)
# print(f"the chai type is {chai_type}")

chai_type.insert(2,"ginger")# 
print(f"the chai type is {chai_type}")
#insert method is used to add the element at specific index in the list
chai_type1=['water','tea','suger','milk']
#pop
suger_type =chai_type1.pop()
print(f"this label retune {suger_type}")# here milek will retrun 
print(f"the chai type is {chai_type1}")#last vaule will remove means milke wiil remove 

#max,mini 
ind=["100","3000","200","300" ]
print(f"the max value is {max(ind)}")#3000
print(f"the min value is {min(ind)}")#100