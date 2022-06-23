# def reverse_num(n):
#     if n<1:
#         return
#     num.append(str(n%10))
#     reverse_num(n//10)
# num=[]
# reverse_num(6543)
# print("".join(num))
num=0

def reverse_num(n):
    global num
    if n<1:
        return
    num=num*10+int(n%10)
    reverse_num(n//10)
reverse_num(6543)
print(num)