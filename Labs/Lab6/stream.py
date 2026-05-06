def generate_data(n):
    for i in range(n):
        yield f"value{i}"
        
def read_stream(source):
    for item in source:
        yield item.strip()
        
def process_stream(sourse, fn):
    for item in sourse:
        yield fn(item)
        
async def async_read_stream(source):
    for item in source:
        yield item.strip()
        
async def async_process_stream(source, fn):
    async for item in source:
        yield fn(item)