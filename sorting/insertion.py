def insertion(lst):
    n=len(lst)
    
    for i in range(1,n):
        x=lst[i]
        j=i-1
        while j>=0 and lst[j]>x :
            lst[j+1]=lst[j]
            j-=1
        lst[j+1]=x
    return lst
lst=[1,53,245,743,3,2,53,22562,7,2,6]
result=insertion(lst)
print(lst)    

        

        