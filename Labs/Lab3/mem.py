from functools import wraps

def memo(max_size=None):
    cache = {}

    def decorator(func):
        @wraps(func)

        def wrapper(*args, **kwargs):
            key = str(args) + str(kwargs)

            if key in cache:
                return cache[key]
            
            res = func(*args, **kwargs)

            if max_size is not None and len(cache) >= max_size:
                first_key = next(iter(cache))
                del cache[first_key]
                
            cache[key] = res

            return res
        return wrapper
    return decorator
