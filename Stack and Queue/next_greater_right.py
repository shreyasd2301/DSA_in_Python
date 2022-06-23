# def solve(arr):
#     op=[]
    
#     for i in range(len(arr)):
#         a=-1
#         for j in range(i+1,len(arr)):
#             if arr[j]>arr[i]:
#                 a=arr[j]
#                 break
#         op.append(a)
#     return op
# arr=[1,3,2,4]
# print(solve(arr))


def solve(arr):
    stack=[]
    op=[]
    for i in range(len(arr)-1,-1,-1):
        if len(stack)==0:
            op.append(-1)
        elif stack[-1]>arr[i]:
            op.append(stack[-1])
        else:
            while stack[-1]<arr[i] and len(stack)>0:
                stack.pop(-1)
            if len(stack)==0:
                op.append(-1)
            if stack[-1]>arr[i]:
                op.append(stack[-1])
        stack.append(arr[i])
    return op
        
arr=[1,3,2,4]
#arr=[11, 13, 21, 3]
op=solve(arr)
print(op[::-1])