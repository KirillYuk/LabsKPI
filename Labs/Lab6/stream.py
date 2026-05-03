def generate_data(n):
    for i in range(n):
        yield f"value{i}"
        
def read_stream(source):
    for item in source:
        yield item.strip()