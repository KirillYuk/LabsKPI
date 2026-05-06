import asyncio
import tracemalloc
from stream import generate_data, read_stream, process_stream, async_process_stream, async_read_stream


def to_upper(item):
    return item.upper()

def add_index(item):
    return "[processed]", item



for item in read_stream(generate_data(5)):
    print(item)
    

pipeline = process_stream(read_stream(generate_data(5)), to_upper)
for item in pipeline:
    print(item)
    
    
async def demo_async():
    source = async_read_stream(generate_data(5))
    async for item in async_process_stream(source, add_index):
        print(item)
asyncio.run(demo_async()) 


tracemalloc.start()
data = list(generate_data(100000))
current, peak = tracemalloc.get_traced_memory()
print("without stream, peak memory: ", peak/1024, "KB")
tracemalloc.stop()

tracemalloc.start()
pipeline = process_stream(read_stream(generate_data(100000)), to_upper)
for item in pipeline:
    pass
current, peak = tracemalloc.get_traced_memory()
print("with stream, peak memory: ", peak/1024, "KB")
tracemalloc.stop()
