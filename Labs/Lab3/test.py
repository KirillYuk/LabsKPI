from mem import memo

@memo(max_size=2, strategy="lru")
def multiply(x, y=2):
    print("calc", x, "*", y)
    return x * y

print(multiply(x = 2, y = 3))
print(multiply(y = 3, x = 2))