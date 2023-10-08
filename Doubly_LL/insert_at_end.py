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
def insertend(head,key):
    temp=Node(key)
    if head==None:
        return temp
    cur=head
    while cur.next!=None:
        cur=cur.next
    cur.next=temp
    temp.prev=cur
    return head
head=None #explain this line why this is important
head=insertend(head,10)
head=insertend(head,20)
head=insertend(head,30)
printlist(head)
