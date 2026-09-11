import asyncio
import threading
import time

def background_task():
    while True:
        print(f"Background task running in thread")
        time.sleep(1)   

async def fetch_data():
        await asyncio.sleep(2)  
        print(f"Fetch data completed in thread")

threading.Thread(target=background_task, daemon=True).start()

asyncio.run(fetch_data())

