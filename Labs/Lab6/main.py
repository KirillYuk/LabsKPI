from stream import generate_data, read_stream

for item in read_stream(generate_data(5)):
    print(item)