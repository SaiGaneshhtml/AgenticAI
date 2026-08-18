# here we learn threading 
# we use mult thread to done task 
# use core (processer ) with muti thread we will achive the task
# eg at a tea shop 1 guy who take order and server tea he peform task ascho.io 
# 1 tacke order then server like this 
import threading
import time

def take_order():
    for i in range(1,8):
     print(f"tacking order : {i}")
     time.sleep(0.2)# sleep 2 sec rest

def serveing_order():
    for i in range(1,8):
     print(f"serving  order : {i}")
     time.sleep(0.3)# sleep 2 sec rest

# 2 func are defin now we  use threading
# in theading we need give target 
take_order = threading.Thread(target=take_order)
serveing_order= threading.Thread(target=serveing_order)
# here we assing the threads only now need start 

take_order.start()
serveing_order.start()

# now need end or join the task

take_order.join()
serveing_order.join()

print('done')