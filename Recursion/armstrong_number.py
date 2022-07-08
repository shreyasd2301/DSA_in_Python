def length_of_number(num):
    global length
    length+=1
    if num<10:
        return
    length_of_number(num//10)

def armstrong_number(num):
    global op
    op=op+(num%10)**length
    if num<10:
        return
    armstrong_number(num//10)

num=1634
length=0
length_of_number(num)
op=0
armstrong_number(num)

if op==num:
    print("Armstrong Number")
else:
    print("Not a Armstrong Number")
