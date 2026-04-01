import asyncio
import time
import json
import aiohttp
import requests

URLS = {
    "data1.json": "https://jsonplaceholder.typicode.com/posts",
    "data2.json": "https://jsonplaceholder.typicode.com/users",
    "data3.json": "https://jsonplaceholder.typicode.com/comments",
    "data4.json": "https://jsonplaceholder.typicode.com/todos",
}


async def fetch(session, filename, url):
    r = await session.get(url)
    data = await r.json()
    with open(filename, "w") as f:
        json.dump(data, f)

async def main():
    start = time.perf_counter()
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(
            fetch(session, "data1.json", URLS["data1.json"]),
            fetch(session, "data2.json", URLS["data2.json"]),
            fetch(session, "data3.json", URLS["data3.json"]),
            fetch(session, "data4.json", URLS["data4.json"]),
        )
    end = time.perf_counter()
    print(f"Async time: {end - start:.2f}s")


def request():
    start = time.perf_counter()
    for filename, url in URLS.items():
        r = requests.get(url)
        data = r.json()
        with open(filename, "w") as f:
            json.dump(data, f)
    end = time.perf_counter()
    print(f"Sync time: {end - start:.2f}s")

asyncio.run(main())
request()