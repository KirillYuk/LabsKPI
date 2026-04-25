import time
import asyncio
from async_map import async_map_promise, async_map_await


async def double(x):
    await asyncio.sleep(1) 
    return x * 2

async def main():
    cancel = asyncio.Event()
    
    async def cancel_after():
        await asyncio.sleep(2)
        cancel.set()
        print("cancel signal")
    
    asyncio.create_task(cancel_after())
    result = await async_map_await([1, 2], double, cancel)
    print("result", result)
    
asyncio.run(main())