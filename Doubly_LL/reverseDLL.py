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
def reverse(head):
    if head==None:
        return None
    if head.next==None:
        return head
    cur=head
    prev=None
    while cur!=None:
        prev=cur
        cur.next,cur.prev=cur.prev,cur.next
        cur=cur.prev
    return prev
head = Node(10)
temp1 = Node(20)
temp2 = Node(30)

head.next = temp1
temp1.prev = head

temp1.next = temp2
temp2.prev = temp1

printlist(head)

head = reverse(head)

printlist(head)