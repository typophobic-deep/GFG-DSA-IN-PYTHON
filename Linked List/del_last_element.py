class Node:
    def __init__(self,key):
        self.key=key
        self.next=None

def delete(head):
    if head==None:
        return None
    if head.next==None:
        return None
    cur=head
    while cur.next.next!=None:
        cur=cur.next
    cur.next=None
    return head 
    
def printlist(head):
    cur=head
    while(cur!=None):
        print(cur.key,end=" ")
        cur=cur.next    
    print()
        
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

printlist(head)
head=delete(head)
printlist(head)         
