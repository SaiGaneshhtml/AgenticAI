# here we learn the retune 
#they are 3 types of return
# 1 is return with no value, 2 is return with single value
# , 3 is return with multiple value


def man ():
    pass
print(man())# it retun none because we use pass and no return value

def woman():
    return 'hello'

hello_womane = woman()# here we store the return value in a variable hello_womane
print(hello_womane)

def child():
    return 'sai', '24'
name , age  = child()# here we store the return value in a variable name and age

print(name, age)# here we print the individual values
print('name: ', name, 'age: ', age,)# here we return multiple value and print it directly
