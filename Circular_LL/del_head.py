class Node:
    def __init__(self,key):
        self.key=key
        self.next=None
def delhead(head):
    if head==None:
        return None
    elif head.next==None:
        return None
    cur=head
    while cur.next!=head:
        cur=cur.next
    cur.next=head.next
    return cur.next
def printlist(head):

    if head==None:
        return
    print(head.key,end=" ")
    cur=head.next
    while cur!=head:
        print(cur.key,end=" ")
        cur=cur.next
    print()
head = Node(20)
head.next = Node(30)
head.next.next = head
printlist(head)
head = delhead(head)

printlist(head)           