def bubble(lst):
    n=len(lst)
    for i in range(n-1):
        for j in range(n-1-i):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
    return lst
lst=[1,56,43,25,67,2]
result=bubble(lst)
print(result)            