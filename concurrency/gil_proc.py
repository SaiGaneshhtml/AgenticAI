# threading 

from multiprocessing import Process
import time

def tea_time():
    print("befor processing ")
    count = 0
    for _ in range(1_00_00_00_00):
        count +=1

    print("after  processing")

if __name__=='__main__':
    p1 = Process(target=tea_time)
    p2 = Process(target=tea_time)

    start= time.time()
#start
    p1.start()
    p2.start()
#join {join all the task}
    p1.join()
    p2.join()
    end = time.time()
    print(f"doen{end - start:.2f}")



