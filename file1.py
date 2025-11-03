import math
import random
import statistics

def generate_numbers(n, start=1, end=100):
    return [random.randint(start, end) for _ in range(n)]

def mean(numbers):
    return statistics.mean(numbers)

def median(numbers):
    return statistics.median(numbers)

def variance(numbers):
    return statistics.variance(numbers)

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq

def circle_area(radius):
    return math.pi * radius ** 2

def distance(p1, p2):
    return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)

def prime_numbers(limit):
    primes = []
    for num in range(2, limit+1):
        if all(num % p != 0 for p in range(2, int(math.sqrt(num))+1)):
            primes.append(num)
    return primes

def random_operations():
    nums = generate_numbers(10)
    print("Numbers:", nums)
    print("Mean:", mean(nums))
    print("Median:", median(nums))
    print("Variance:", variance(nums))
    print("Primes:", prime_numbers(50))
    print("Numbers (v5):", nums)
    print("Running version E — duplicate 5, experimental mode")

   
    print("Numbers (v4):", nums)
    print("Running version D — duplicate 4, new constants")


if __name__ == "__main__":
    random_operations()
