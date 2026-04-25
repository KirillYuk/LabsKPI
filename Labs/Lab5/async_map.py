import asyncio


def sync_map(arr, fn):
    result = []
    for item in arr:
        result.append(fn(item))
    return result


def async_map_callback(arr, fn, callback):
    async def run():
        try:
            results = await asyncio.gather(*[fn(item) for item in arr])
            callback(None, results)
        except Exception as e:
            callback(e, None)
    asyncio.run(run())


async def async_map_promise(arr, fn):
    results = await asyncio.gather(*[fn(item) for item in arr])
    return results


async def async_map_await(arr, fn):
    results = []
    for item in arr:
        result = await fn(item)
        results.append(result)
    return results