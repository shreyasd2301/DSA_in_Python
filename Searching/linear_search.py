from re import I


def linear_search(ele, arr):
    id=-1
    for i in range(len(arr)):
        if arr[i]==ele:
            id=i
            break
    return id
arr=[2,56,6,8,88]
print(linear_search(8, arr))