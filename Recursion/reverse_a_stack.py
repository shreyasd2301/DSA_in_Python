def reverse_stack(n):
    b.append(n.pop())
    if len(n)==1:
        b.append(n.pop())
        return
    reverse_stack(n)

b=[]
a=[1,2,3,4]
reverse_stack(a)
print(b)