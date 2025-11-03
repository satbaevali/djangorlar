import math
import random

def fibonacci(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    total = sum(result)
    print("Total Fibonacci sum:", total)
    return result

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def primes_up_to(limit):
    primes = []
    for x in range(2, limit + 1):
        if is_prime(x):
            primes.append(x)
    return primes

def random_math_
