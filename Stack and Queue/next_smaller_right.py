def solve(arr):
    op=[]
    stack=[]
    for i in range(len(arr)-1,-1,-1):
        if len(stack)==0:
            op.append(-1)
        elif stack[-1]<arr[i]:
            op.append(stack[-1])
        else:
            while len(stack)>0 and stack[-1]>arr[i]:
                stack.pop(-1)
            if len(stack)==0:
                op.append(-1)
            if stack:
                if stack[-1]<arr[i]:
                    op.append(stack[-1])
        stack.append(arr[i])
    return op

arr=[11, 13, 21, 3]
arr=[1,3,2,4]
print(solve(arr)[::-1])