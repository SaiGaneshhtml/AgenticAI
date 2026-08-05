name =[
    'sai', 
    'alice',
    'bob',
    'ganesh'
]
# lsir = [expresstion for iteam in iterable if condition]
# in the exp my_name is expression, name is iterable and len(my_name) > 5 is condition
name = [my_name for my_name in name if len(my_name) > 5]

print(name)