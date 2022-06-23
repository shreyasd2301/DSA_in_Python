arr= [3,4,1,5,2]
l=len(arr)

for i in range(4):
    
    for i in range(l-1):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i] 
    l-=1   

print(arr)