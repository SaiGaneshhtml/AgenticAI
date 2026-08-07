# we acutall send  data to yield 
#usinf send we can send msg to yield
def cups():
    print("Start")
    order = yield # start
    while True:
        print(f"Order received: {order}")
        order = yield # stop 

stall = cups()
next(stall) 
stall.send("tea")
stall.send("coffee")
