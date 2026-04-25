import time
import asyncio
from async_map import async_map_promise, async_map_await, sync_map, async_map_callback


async def double(x):
    await asyncio.sleep(1) 
    return x * 2


print("sync")
print(sync_map([1,2,3], lambda x: x*2))


print("callback")
def on_done(err, result):
    if err:
        print("err: ", err)
    else:
        print("resulr: ", result)
async_map_callback([1, 2, 3], double, on_done)


print("promise")
async def my_promise():
    start = time.time()
    result = await async_map_promise([1,2,3], double)
    print("result", result, time.time() - start, "sec")
asyncio.run(my_promise())


print("async/await")
async def my_await():
    start = time.time()
    result = await async_map_await([1,2,3], double)
    print("result: ", result, time.time() - start, "sec")
asyncio.run(my_await())


print("canceling")
async def my_cancel():
    cancel = asyncio.Event()
    
    async def cancel_after():
        await asyncio.sleep(2)
        cancel.set()
        print("!cancel signal!")
    
    asyncio.create_task(cancel_after())
    result = await async_map_await([1, 2], double, cancel)
    print("result", result)
    
asyncio.run(my_cancel())