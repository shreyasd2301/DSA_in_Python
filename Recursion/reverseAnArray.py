# def reverse_array(b):
#     if len(b)==1:
#         a.append(b[0])
#         return
#     reverse_array(b[1:])
#     a.append(b[0])
# b=[1,2,3]
# a=[]
# reverse_array(b)
# print(a)

# extra space is taken by a
# trying to do by using same array

a=[1,2,3,4]
def reverse_array(n):
    if len(n)==1:
        return
    x=n.pop(0)
    reverse_array(n)
    n.append(x)

reverse_array(a)
print(a)