def power_of_two(n):
    if n==1:
        return 2
    return 2*power_of_two(n-1)
print(power_of_two(3))