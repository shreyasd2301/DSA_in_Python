def fib(n):
    if n==2:
        return 1
    if n==1:
        return 0
    return fib(n-1)+fib(n-2)

print(fib(3))