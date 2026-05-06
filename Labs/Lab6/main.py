import asyncio
import tracemalloc
from stream import generate_data, read_stream, process_stream, async_process_stream, async_read_stream


def to_upper(item):
    return item.upper()

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