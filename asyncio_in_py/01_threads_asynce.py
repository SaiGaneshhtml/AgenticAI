import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

def stock_price(stock):
    print(f"Fetching price for {stock}...")
    time.sleep(2)  # Simulate a delay in fetching the stock price
    return f"Price of {stock}: ${100 + hash(stock) % 50}"  # Simulated stock price

async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as power:
      results = await loop.run_in_executor(power,stock_price, "AAPL")
      print(results)

asyncio.run(main())
