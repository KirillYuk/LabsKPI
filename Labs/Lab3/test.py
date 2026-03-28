from mem import memo

@memo(max_size=2)
def multiply(x, y=1):
    print("calc", x, "*", y)
    return x * y

print(multiply(3))
print(multiply(4))
print(multiply(5))
print(multiply(3))
print(multiply(5, 5))
print(multiply(5, 3))
print(multiply(5, 5))