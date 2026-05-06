import asyncio
from stream import generate_data, read_stream, process_stream, async_process_stream, async_read_stream


def to_upper(item):
    return item.upper()

async def main():
    source = async_read_stream(generate_data(5))
    async for item in async_process_stream(source, to_upper):
        print(item)
        
asyncio.run(main())