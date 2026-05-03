def generate_data(n):
    for i in range(n):
        yield f"value{i}"
        
def read_stream(source):
    for item in source:
        yield item.strip()
        
def process_stream(sourse, fn):
    for item in sourse:
        yield fn(item)