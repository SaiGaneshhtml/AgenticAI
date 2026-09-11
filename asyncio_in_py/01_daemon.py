# deamon thread example
# we use deamon thread to run background when task will done 
# the deamon thread will automatically terminate when the main program exits, 
# so we don't have to worry about stopping it manually.
import time
import threading

def background_task():
    while True:
        print(f"Background task running in thread")
        time.sleep(1)

t1=threading.Thread(target=background_task, daemon=True)
t1.start()

