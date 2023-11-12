def selection(lst):
    n=len(lst)
    for i in range(n-1):
        min=i
        for j in range(i+1,n):
            if lst[j]<lst[min]:
                min=j
        lst[i],lst[min]=lst[min],lst[i]   
    return lst       
lst=[1,5,7,4,8,9,3,73,23,2224,2,422,0]
result=selection(lst)
print(result)  