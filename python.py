print("Shubham Jadhav 21153")
def fibonacci(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

# Taking input from user for the number of terms
num_terms = int(input("Enter the number of Fibonacci terms: "))

# Generate and print the Fibonacci series
fib_result = fibonacci(num_terms)
print("Fibonacci Series:")
print(fib_result)
