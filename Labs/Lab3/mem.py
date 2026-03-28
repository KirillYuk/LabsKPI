import time
from functools import wraps


def memo(max_size=None, strategy="lru"):
    cache = {}
    access_time = {}

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            key = str(args) + str(kwargs)
            now = time.time()

            if key in cache:
                access_time[key] = now
                return cache[key]

            res = func(*args, **kwargs)

            if max_size is not None and len(cache) >= max_size:
                if strategy == "lru":
                    to_del = min(access_time, key=access_time.get)
                else:
                    to_del = next(iter(cache))

                del cache[to_del]
                del access_time[to_del]

            cache[key] = res
            access_time[key] = now

            return res

        return wrapper

    return decorator
