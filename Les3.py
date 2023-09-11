def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Использование генератора для генерации первых 10 чисел Фибоначчи
fib = fibonacci_generator()
for i in range(10): # Генерируем первые 10 чисел Фибоначчи
    print(next(fib))
