def sort_array(n):
    if len(n)==1:
        return 
    x=n.pop()
    sort_array(n)
    insert_array(x,n)

def insert_array(x,n):
    if len(n)==0 or n[-1]<x:
        n.append(x)
        return 
    y=n.pop()
    insert_array(x,n)
    n.append(y)
    
a=[1,3,4,2]
sort_array(a)
print(a)