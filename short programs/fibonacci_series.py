def fibonacci(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

n = 6
print(f"Fibonacci series up to {n} terms:", fibonacci(n))
