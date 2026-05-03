from stream import generate_data, read_stream, process_stream


def to_upper(item):
    return item.upper()

pipeline = process_stream(read_stream(generate_data(5)), to_upper)

for item in pipeline:
    print(item)