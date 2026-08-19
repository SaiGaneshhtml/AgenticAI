from multiprocessing import Process , Queue , Value

def inc (count):
    for _ in range(100000):
        with count.get_lock():
            count.value +=1

if __name__=='__main__':
    count = Value('i',0)
    process = [Process(target=inc,args=(count,)) for _ in range (4)]
    [p.start() for p in process]
    [p.join() for p in process]


    print('here final vaule', count.value)



    