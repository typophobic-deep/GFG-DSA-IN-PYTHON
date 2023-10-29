class Node:
    def __init__(self,key):
        self.key=key
        self.next=None
def delhead(head):
    cur=head
    cur.key=cur.next.key
    cur.next=cur.next.next
    return cur        
def delete(head,k):
    if head==None:
        return None
    elif k==1:
        return delhead(head)        
    else:
        cur=head
        for i in range(k-2):
            cur=cur.next
        cur.next=cur.next.next
        return head
def printlist(head):
    if head==None:
        return
    print(head.key,end=" ")
    cur=head.next
    while cur!=head:
        print(cur.key,end=" ")
        cur=cur.next
    print()           
head=Node(10)    
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=head
printlist(head)
head=delete(head,2)
printlist(head)