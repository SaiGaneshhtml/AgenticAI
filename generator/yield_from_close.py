# we will knwo form ad close 

def ganesh():
    yield "ganesh"

def sai():
    yield "sai"

def full_name():
    yield from ganesh()
    yield from sai()

name = full_name()
print(next(name))
print(next(name))

def order():

    try:
        while True:
          name = yield "this is my full name"
    except:
        print("this is invalied name")


stall = order()
print(next(stall))
stall.close()# cleaen the memory 