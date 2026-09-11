import time
import threading

def background_task():
    while True:
        print(f"Background task running in thread")
        time.sleep(1)

t1=threading.Thread(target=background_task)
t1.start()

# without daemon thread, the program will not exit until 
# the background task is manually stopped.