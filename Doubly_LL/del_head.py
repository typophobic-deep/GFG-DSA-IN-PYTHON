class Node:
    def __init__(self,key):
        self.key=key
        self.next=None
        self.prev=None
def printlist(head):
    cur=head 
    while cur!=None:
        print(cur.key,end=" ")
        cur=cur.next
    print()
def delend(head):
    cur=head 
    if head==None or head.next==None:
        return None
    while cur.next.next!=None:
        cur=cur.next
    cur.next=None    
    return head    
head=Node(10)
head.next=Node(20)    
head.next.next=Node(30)
head.next.next.next=Node(40)
printlist(head)
head=delend(head)

printlist(head)

