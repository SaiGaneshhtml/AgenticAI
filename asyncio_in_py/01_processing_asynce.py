import asyncio
from concurrent.futures import ProcessPoolExecutor

def card(data):
    return f"Card for {data[::-1]}"

async def main():
    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor() as executor:
        results = await loop.run_in_executor(executor, card, "11233_card")
        print(results)


if __name__ == "__main__":
    asyncio.run(main())