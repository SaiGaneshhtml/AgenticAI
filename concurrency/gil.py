# threading 

import threading 
import time

def tea_time():
    print("befor threading ")
    count = 0
    for _ in range(1_00_00_00_00):
        count +=1

    print("after  threading")

thread1 = threading.Thread(target=tea_time,name='threading1')
thread2 = threading.Thread(target=tea_time,name='threading2')

start= time.time()
#start
thread1.start()
thread2.start()
#join {join all the task}
thread1.join()
thread2.join()
end = time.time()
print(f"doen{end - start:.2f}")

