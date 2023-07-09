def log_decorator(func):
    def wrapper(*args, **kwargs):
        print("Calling function...")
        result = func(*args, **kwargs)
        print("Function called.")
        return result
    return wrapper

@log_decorator
def add(x, y):
    return x + y

result = add(2, 3)
print(result) # Output: Calling function... Function called. 5


def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci(10):
    print(num) # Output: 0 1 1 2 3 5 8 13 21 34

