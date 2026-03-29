import time
from functools import wraps


def memo(max_size=None, strategy="lru", ttl=None, custom=None):
    cache = {}
    access_time = {}
    create_time = {}
    use_count = {}

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            key = str(args) + str(sorted(kwargs.items()))
            now = time.time()

            if ttl is not None and key in cache:
                if now - create_time[key] > ttl:
                    del cache[key]
                    del create_time[key]
                    del access_time[key]
                    del use_count[key]

            if key in cache:
                access_time[key] = now
                use_count[key] = use_count[key] + 1
                return cache[key]

            res = func(*args, **kwargs)

            if max_size is not None and len(cache) >= max_size:
                if custom is not None:
                    to_del = custom(cache, access_time, use_count)
                elif strategy == "lru":
                    to_del = min(access_time, key=access_time.get)
                elif strategy == "lfu":
                    to_del = min(use_count, key=use_count.get)
                else:
                    to_del = next(iter(cache))

                del cache[to_del]
                del access_time[to_del]
                del create_time[to_del]
                del use_count[to_del]

            cache[key] = res
            access_time[key] = now
            create_time[key] = now
            use_count[key] = 1

            return res

        return wrapper

    return decorator
