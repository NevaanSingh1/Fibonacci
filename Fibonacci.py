# Fibonacci.py

def fibonacci_series(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

if __name__ == "__main__":
    try:
        n = int(input("Enter the number of terms: "))
        if n <= 0:
            print("Please enter a positive integer.")
        else:
            print("Fibonacci series up to", n, "terms:")
            print(fibonacci_series(n))
    except ValueError:
        print("Invalid input. Please enter an integer.")