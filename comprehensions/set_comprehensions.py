# here we learn about set comprehensions

number = ['1', '2', '3','2','3','2','3','2','3','2','1','2','3']
# in set we no need to give filter condition because set will
#  automatically remove duplicates
unique_numbers = {x for x in number}    
print(unique_numbers)

# if we have dictonary and we want to get unique values from it then we can use set comprehension

coffee = {
    'black': ('water','coffee powder', 'sugar'),
    'normal': ('water','coffee powder', 'milk', 'sugar'),
    'cold': ('water','coffee powder', 'milk', 'sugar', 'ice'),
    'hot': ('water','coffee powder', 'milk', 'sugar', 'ice', 'cinnamon')
}

# if we too get unique values from the above dictonary then we can use set comprehension
# usale the we use iterable in the expression but in set dictionary 
# we can use values() method to get the values from the dictionary and then 
# we can use for loop to get the unique values from it.
# here flavor is expression, ingredients is iterable and coffee.values() is iterable
# ingredinats store the  ('water','coffee powder', 'sugar')
# flavor store the unique ingredients
unique_ingredients = {flavor for ingredients in coffee.values() for flavor in ingredients}
print(unique_ingredients)