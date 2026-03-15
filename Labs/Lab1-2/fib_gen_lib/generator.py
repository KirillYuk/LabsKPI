import time

def fib_gen():
    a = 0
    b = 1
    while True:
        yield a
        next_val = a + b
        a = b
        b = next_val

def run(iterator, seconds):
    end_time = time.time() + seconds
    print(f"Working {seconds} seconds")
    for val in iterator:
        if time.time() > end_time:
            break
        print(val)
        time.sleep(0.1)
