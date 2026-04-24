import asyncio


# def sync_map(arr, fn):
#     result = []
#     for item in arr:
#         result.append(fn(item))
#     return result


def async_map_callback(arr, fn, callback):
    async def run():
        results = await asyncio.gather(*[fn(item) for item in arr])
        callback(results)

    asyncio.run(run())