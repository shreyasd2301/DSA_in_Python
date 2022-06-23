def print_num(n):
    if n==1:
        print(1)
        return
    print(n)
    print_num(n-1)
    

print_num(5)