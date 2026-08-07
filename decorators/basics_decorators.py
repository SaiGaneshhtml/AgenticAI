# decorators
from functools import wraps# help  meta data 
def my_decorator(fun):
    @wraps(fun)
    def wrapper():
        print("befor")
        fun()
        print("after")
    return wrapper

@my_decorator

def greet():
    print("this fun pass in the warpper")

greet()
print(greet.__name__)# show name insted of wrapper