def fib(n):
    if n == 0 or n == 1:
        print(n)
        return n
    else:
        print(n)
        return fib(n-1)+fib(n-2)

print(fib(int(input("Enter a number: "))))
