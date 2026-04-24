import asyncio
from async_map import async_map_promise


async def double(x):
    await asyncio.sleep(1) 
    return x * 2

async def main():
    result = await async_map_promise([2, 1, 8], double)
    print("result: ", result)

asyncio.run(main())