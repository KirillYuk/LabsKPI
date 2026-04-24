import asyncio
from async_map import async_map_callback


async def double(x):
    await asyncio.sleep(1) 
    return x * 2

def on_done(result):
    print(result)

async_map_callback([1, 2, 3], double, on_done)