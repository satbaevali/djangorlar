import math
import random
import time

def fibonacci(n):
    start = time.time()
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    print("Execution time:", round(time.time() - start, 6), "s")
    return result

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

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

def random_math_demo():
    nums = [random.randint(1, 30) for _ in range(8)]
    print("Duplicate-2 numbers:", nums)
    print("Average:", round(sum(nums) / len(nums), 2))

def main():
    print("Version: duplicate-2")
    print("Fibonacci:", fibonacci(12))
    print("Factorial of 5:", factorial(5))
    print("Primes up to 30:", primes_up_to(30))
    random_math_demo()

if __name__ == "__main__":
    main()
