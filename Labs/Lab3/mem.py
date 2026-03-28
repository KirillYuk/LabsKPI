from functools import wraps

def memo():
    cache = {}

    def decorator(func):
        @wraps(func)

        def wrapper(*args, **kwargs):
            key = str(args) + str(kwargs)

            if key in cache:
                return cache[key]
            
            res = func(*args, **kwargs)
            cache[key] = res

            return res
        return wrapper
    return decorator
