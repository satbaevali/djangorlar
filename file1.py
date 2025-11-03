import math
import random

def fibonacci(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

def factorial(n):
    return math.prod(range(1, n + 1))

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def primes_up_to(limit):
    return [x for x in range(2, limit + 1) if is_prime(x)]

def random_math_demo():
    nums = [random.randint(1, 20) for _ in range(10)]
    squares = [x**2 for x in nums]
    roots = [round(math.sqrt(x), 2) for x in nums]
    print("Numbers:", nums)
    print("Squares:", squares)
    print("Roots:", roots)

def main():
    print("Fibonacci:", fibonacci(10))
    print("Factorial of 6:", factorial(6))
    print("Primes up to 50:", primes_up_to(50))
    random_math_demo()

if __name__ == "__main__":
    main()
