import asyncio
from async_map import async_map_promise, async_map_await, sync_map, async_map_callback

print("TESTS\n")


async def double(x):
    return x * 2


result = sync_map([1, 2, 3], lambda x: x * 2)
if result == [2, 4, 6]:
    print("sync map: PASS")
else:
    print("sync map: FAIL")


callback_result = None
def on_done(error, result):
    global callback_result
    callback_result = result

async_map_callback([1, 2, 3], double, on_done)
if callback_result == [2, 4, 6]:
    print("callback: PASS")
else:
    print("callback: FAIL")


async def test_promise():
    result = await async_map_promise([1, 2, 3], double)
    if result == [2, 4, 6]:
        print("promise: PASS")
    else:
        print("promise: FAIL")
asyncio.run(test_promise())


async def test_await():
    result = await async_map_await([1, 2, 3], double)
    if result == [2, 4, 6]:
        print("async/await: PASS")
    else:
        print("async/await: FAIL")
asyncio.run(test_await())


async def test_empty():
    result = await async_map_await([], double)
    if result == []:
        print("empty array: PASS")
    else:
        print("empty array: FAIL")
asyncio.run(test_empty())


async def slow_double(x):
    await asyncio.sleep(1)
    return x * 2

async def test_cancel():
    cancel = asyncio.Event()

    async def cancel_after():
        await asyncio.sleep(2.5)
        cancel.set()

    asyncio.create_task(cancel_after())
    result = await async_map_await([1, 2, 3, 4, 5], slow_double, cancel)
    if result is None:
        print("cancel: PASS")
    else:
        print("cancel: FAIL")

asyncio.run(test_cancel())