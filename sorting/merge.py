def mergesort(arr,l,r):
    if l<r:
        mid=(l+r)//2
        mergesort(arr,l,mid)
        mergesort(arr,mid+1,r)
        merge(arr,l,mid,r)
def merge(arr,l,mid,h):
    left=arr[l:mid+1]
    right=arr[mid+1:h+1]
    i=0
    j=0
    k=l
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            arr[k]=left[i]
            k+=1
            i+=1
        else:
            arr[k]=right[j]
            j+=1
            k+=1
    while i<len(left):
        arr[k]=left[i]
        i+=1
        k+=1
    while j<len(right):
        arr[k]=right[j]
        j+=1
        k+=1
    
arr=[1,3,5,4345,7473,27,7,27,7,0]                
mergesort(arr,0,len(arr)-1)
print(*arr)
