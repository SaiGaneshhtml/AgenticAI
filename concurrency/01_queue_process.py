from multiprocessing import Process , Queue

def chai_maker(queue):
    queue.put('hello')

if __name__=='__main__':
    queue = Queue()

    p=Process(target=chai_maker,args=(queue,))
    p.start()
    p.join()
    print(queue.get())