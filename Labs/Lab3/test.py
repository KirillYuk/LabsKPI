import time
from mem import memo

print("TESTS")


call_count = 0


@memo()
def cache_test(x):
    global call_count
    call_count += 1
    return x * 10


cache_test(3)
cache_test(3)
cache_test(3)

if call_count == 1:
    print("Cache: PASS")
else:
    print("Cache: FAIL")


call_count = 0


@memo(max_size=2, strategy="lru")
def lru_test(x):
    global call_count
    call_count += 1
    return x * 10


lru_test(1)
lru_test(2)
lru_test(1)
lru_test(3)
lru_test(2)

if call_count == 4:
    print("LRU: PASS")
else:
    print("LRU: FAIL")


call_count = 0


@memo(max_size=2, strategy="lfu")
def lfu_test(x):
    global call_count
    call_count += 1
    return x * 10


lfu_test(1)
lfu_test(1)
lfu_test(2)
lfu_test(3)
lfu_test(2)

if call_count == 4:
    print("LFU: PASS")
else:
    print("LFU: FAIL")


call_count = 0


@memo(ttl=1)
def ttl_test(x):
    global call_count
    call_count += 1
    return x * 10


ttl_test(5)
ttl_test(5)
time.sleep(1.5)
ttl_test(5)

if call_count == 2:
    print("TTL: PASS")
else:
    print("TTL: FAIL")


call_count = 0


def my_custom(cache, access_time, use_count):
    return max(cache, key=cache.get)


@memo(max_size=2, custom=my_custom)
def custom_test(x):
    global call_count
    call_count += 1
    return x * 10


custom_test(5)
custom_test(8)
custom_test(3)
custom_test(8)

if call_count == 4:
    print("Custom: PASS")
else:
    print("Custom: FAIL")
