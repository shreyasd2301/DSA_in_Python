arr= [3,4,1,5,2]
l=len(arr)

for i in range(l-1):
    for j in range(i+1,l):
        if arr[i]>arr[j]:
            arr[i],arr[j]=arr[j],arr[i]   

print(arr)