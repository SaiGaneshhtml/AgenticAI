import asyncio

async def chai(name):
    print(f"Hello, {name}!")
    await asyncio.sleep(2)
    print(f"Goodbye, {name}!")

async def main():
    await asyncio.gather(
        chai("Alice"),
        chai("Bob"),
        chai("Charlie")
    )

asyncio.run(main())