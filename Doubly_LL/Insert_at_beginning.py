class Node:
    def __init__( self,key):
        self.key=key
        self.prev=None
        self.next=None
def printlist(head):
    cur=head
    while cur!=None:
        print(cur.key,end=" ")
        cur=cur.next
    print()
def insertatbeg(head,key):
    temp=Node(key)
    cur=head
    if head != None:
        head.prev=temp
    temp.next=head
    return temp

head=None
head=insertatbeg(head,10)
head=insertatbeg(head,20)
printlist(head)
head=insertatbeg(head,30)
printlist(head)
            
            