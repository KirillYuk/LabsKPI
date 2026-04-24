import asyncio
from async_map import async_map_callback


async def double(x):
    await asyncio.sleep(1) 
    return x * 2

def on_done(error, result):
    if error:
        print("error: ", error)
    else:
        print("result: ", result)

async_map_callback([2, 3, 4], double, on_done)