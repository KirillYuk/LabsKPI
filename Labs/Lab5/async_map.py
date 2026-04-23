
def sync_map(arr, fn):
    result = []
    for item in arr:
        result.append(fn(item))
        print(result)
    return result

print(sync_map([1, 2, 3], lambda x: x * 2))