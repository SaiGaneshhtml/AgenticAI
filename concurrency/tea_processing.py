#here we us multi cors 

from multiprocessing import Process
import time

def tea_shop(name):
    print(f"befor {name}")
    time.sleep(3)
    print(f"after {name}")

if __name__== '__main__':
    chai_maker=[
        Process(target=tea_shop,args=(f'print {i+1}',))
        for i in range(4)
    ]

    #start the processing 
    for p in chai_maker:
        p.start()

    #stop
    for p in chai_maker:
        p.join()

    print('all done')



