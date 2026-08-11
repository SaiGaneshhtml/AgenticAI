# here we learn use argu , kwarge we can pass and using those we can build the fun

from functools import wraps 

def saiganesh (funcs):

    @wraps(funcs)
    def gun(*argus,**kwargs):
        print("befor")
        result = funcs(*argus ,**kwargs)
        print("after")
        return result
    return gun


@saiganesh
# here we build fun passing  argus and kwagus 
def name(type , age):
    print(f'this is my name  : {type} this my age : {age}')
#here we build 
name('ganesh',24)
name('sai',33)

