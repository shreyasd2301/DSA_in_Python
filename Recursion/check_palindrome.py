# def palindrome(num):
#     if len(num)==0 or len(num)==1:
#         print("Palindrome")
#         return
#     if num[0]==num[-1]:
#         palindrome(num[1:len(num)-2])
#     else :
#         print("Not a Palindrome")
#         return 


# palindrome(str(121))
# num=str(121)
def reverse_number(num):
    global op
    if num<10:
        op=op*10+num
        return
    op=op*10+num%10
    num//=10
    reverse_number(num)
op=0
num=121
reverse_number(num)
if num == op:
    print("palindrome number")
else:
    print("not a palindrome number")
