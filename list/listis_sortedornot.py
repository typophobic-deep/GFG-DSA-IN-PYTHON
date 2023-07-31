



def issorted(arr):

    for i in range(n-1):
        if arr[i]<=arr[i+1]:
            return True
        else:
            return False    
def reverselist(arr):
    start=0 
    end=n-1    
    while(start<end) :
        arr[start] , arr[end]=arr[end],arr[start]
        start+=1
        end-=1
    print()    


n=int(input("enter the amount of number you want to add"))
arr=[]

for i in range(n):
    num=int(input())
    arr.append(num) 
# reverselist(arr)
issorted(arr)

if issorted(arr):
    print("The list is sorted in non-decreasing order.")
else:
    print("The list is not sorted in non-decreasing order.")










        