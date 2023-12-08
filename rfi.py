def fibonacci(n):
    fib_sequence = [0, 1]

    for i in range(2, n):
        next_fib = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_fib)

    return fib_sequence

# Пример использования: вычислить первые 10 чисел Фибоначчи
n = 10
result = fibonacci(n)
print(f"Первые {n} чисел Фибоначчи: {result}")