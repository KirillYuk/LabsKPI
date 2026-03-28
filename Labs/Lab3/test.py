from mem import memo

@memo(max_size=2, strategy="lru")
def multiply(x, y=2):
    print("calc", x, "*", y)
    return x * y

print(multiply(1))
print(multiply(2))
print(multiply(1))
print(multiply(3))
print(multiply(2))
print(multiply(3))
print(multiply(1))