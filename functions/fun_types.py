# there 4 typoes pure, impure , lamda , recersive 

#impure  we should use 
cup = 10
def pure_fun(cup):
    return cup * 100

result = pure_fun(5)
print(result)

# pure function is a function that always produces
#  the same output for the same input and has no side effects. 
# In this case, the `pure_fun` function takes an input `cup` and returns its value multiplied by 100. 
# It does not modify any external state or variables, making it a pure function.
#e.g tack cup as parameter and return the value of cup * 100.

def impure_fun():
    global cup
    cup = cup * 100
    return cup

result = impure_fun()
print(f"impure function result: {result}")


# in impure function, the function modifies the external variable `cup` by multiplying it by 100.

# recursive function is a function that calls itself in order to solve a problem.

def recursive_fun(n):
    print(n)
    if n == 0:
        return (f"done recursion")
    return recursive_fun(n - 1)

result = recursive_fun(5)
print(f"recursive function result: {result}")

#lambda function is a small anonymous function that can take any number of arguments, but can only have one expression.

cupe_type =['1','2','3','4','5','2','3','4','5','2','3','4','5','2','3','4','5']

def filter_cup(cup_type):
    return list(filter(lambda name: name  == '0' or name == '4' or name != '5', cup_type))   

result = filter_cup(cupe_type)
print(f"lambda function result: {result}")