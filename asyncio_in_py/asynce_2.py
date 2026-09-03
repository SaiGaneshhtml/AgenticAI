import asyncio
import aiohttp

async def fetch(session, url):
    #due to vm issue im using ssl=False to avoid SSL certificate verification errors
    async with session.get(url, ssl=False) as response:
        print(f"Status for {url}: {response.status}")  

async def main():
    urls = ["https://www.asyncio.org"]*3
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        await asyncio.gather(*tasks)
        #*tasks is used to unpack the list of tasks into separate arguments for asyncio.gather.

asyncio.run(main())