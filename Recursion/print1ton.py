def print_num(n):
    if n==1:
        print(1)
        return
    print_num(n-1)
    print(n)

print_num(5)