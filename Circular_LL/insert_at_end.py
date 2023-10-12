class Node:
    def __init__(self,key):
        self.key=key
        self.next=None
def printlist(head):
    if head==None:
        return 
    print(head.key,end=" ")
    cur=head.next
    while cur!=head:
        print(cur.key,end=" ")
        cur=cur.next
    print()
def insertatend(head,key):
    temp=Node(key)
    if head==None:
        temp.next=temp
        return temp   
    cur=head
    while cur.next!=head:
        cur=cur.next
    temp.next=cur.next
    cur.next=temp
    return head    
head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=head

printlist(head)
head=insertatend(head,40)
printlist(head)
