import time
import asyncio
from async_map import async_map_promise, async_map_await


async def double(x):
    await asyncio.sleep(1) 
    return x * 2

async def main():
    start = time.time()
    result = await async_map_promise([2, 1, 8], double)
    print("result1: ", result, time.time() - start, "c")

    start = time.time()
    result = await async_map_await([2, 1, 8], double)
    print("result2: ", result, time.time() - start, "c")


asyncio.run(main())