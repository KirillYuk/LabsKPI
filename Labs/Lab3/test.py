import time
from mem import memo


@memo(max_size=2, strategy="lru")
def lru_test(x):
    print("calc", x, "*", x)
    return x * x

print("LRU test")
print(lru_test(1))
print(lru_test(1))
print(lru_test(1))
print(lru_test(2))
print(lru_test(1))
print(lru_test(3))
print(lru_test(2))


@memo(max_size=2, strategy="lfu")
def lfu_test(x):
    print("calc", x, "*", x)
    return x * x

print("LFU test")
print(lfu_test(1))
print(lfu_test(1))
print(lfu_test(2))
print(lfu_test(3))
print(lfu_test(1))
print(lfu_test(2))


@memo(ttl=2)
def ttl_test(x):
    print("calc", x, "*", x)
    return x * x

print("TTL test")
print(ttl_test(2))
print(ttl_test(2))
time.sleep(3)
print(ttl_test(2))
print(ttl_test(2))
time.sleep(1.9)
print(ttl_test(2))


def my_custom(cache, access_time, use_count):
    return max(cache, key=cache.get)

@memo(max_size=2, custom=my_custom)
def custom_test(x):
    print("calc", x, "*", x)
    return x * x

print("CUSTOM test")
print(custom_test(5))
print(custom_test(2))
print(custom_test(8))
print(custom_test(3))
print(custom_test(2))
print(custom_test(8))